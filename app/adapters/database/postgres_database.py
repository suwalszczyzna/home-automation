import uuid
from datetime import datetime
from typing import List

from sqlalchemy import create_engine, MetaData, Column, Table, Text, Float, DateTime, Time, func, ForeignKey, Integer, \
    Boolean
from sqlalchemy.dialects.postgresql import UUID

import logger
from app.domain.devices import Device, Status, TempConfig, Hysteresis
from app.domain.interfaces.abstract_database import AbstractDatabase
from app.domain.operation_modes import Operation
from app.domain.schedulers import LowerCostPower, WaterHeatSchedule, Schedule, Weekday
from app.domain.sensors import TempSensor

log = logger.get_logger("PostgresDB")

metadata = MetaData()

temp_config = Table('temp_config', metadata,
                    Column('config_name', Text, primary_key=True),
                    Column('value', Float, nullable=False)
                    )

temp_history = Table('temp_history', metadata,
                     Column('id', UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
                     Column('sensor', Text, nullable=False),
                     Column('temperature', Float, nullable=False),
                     Column('created', DateTime, nullable=False)
                     )

schedules_types = Table('schedules_types', metadata,
                        Column('id', Text, primary_key=True),
                        Column('type_name', Text)
                        )

schedules = Table('schedules', metadata,
                  Column('id', UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
                  Column('schedule_type_id', Text, ForeignKey('schedules_types.id'), nullable=False),
                  Column('start_time', Time, nullable=False),
                  Column('stop_time', Time, nullable=False),
                  Column('created', DateTime, nullable=False, server_default=func.now())
                  )

schedules_days = Table('schedules_days', metadata,
                       Column('id', UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
                       Column('schedule_id', UUID(as_uuid=True), ForeignKey('schedules.id'), nullable=False),
                       Column('weekday', Integer, nullable=False)
                       )

operation_modes = Table('operation_modes', metadata,
                        Column('id', Text, primary_key=True),
                        Column('name', Text),
                        Column('active', Boolean, default=False),
                        Column('check_schedule', Boolean, default=False),
                        )

smart_devices = Table('smart_devices', metadata,
                      Column('id', UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
                      Column('name', Text, nullable=False),
                      Column('device_id', Text, nullable=False),
                      Column('ip_address', Text, nullable=False),
                      Column('local_key', Text, nullable=False),
                      Column('version', Float, nullable=False),
                      Column('last_status', Boolean, nullable=False, default=False),
                      )

notifier = Table('notifier', metadata,
                 Column('name', Text, primary_key=True),
                 Column('value', Boolean, nullable=False, default=False)
                 )

telegram = Table('telegram', metadata,
                 Column('id', Integer, primary_key=True),
                 Column('chat_id', Text, nullable=False)
                 )

hysteresis = Table('hysteresis', metadata,
                   Column('id', Integer, primary_key=True),
                   Column('status', Boolean, nullable=False),
                   Column('value', Integer, nullable=False)
                   )


class PostgresDB(AbstractDatabase):
    def __init__(self, database_uri: str):
        self.engine = create_engine(database_uri)

    def initialize_db(self):
        metadata.drop_all(bind=self.engine)
        metadata.create_all(bind=self.engine)

        with self.engine.begin() as connection:
            queries = [
                temp_config.insert().values(
                    config_name='max_water_temp',
                    value=50
                ),
                operation_modes.insert().values([
                    {'id': 'auto_mode',
                     'name': 'Pełny automat',
                     'active': True,
                     'check_schedule': False},
                    {'id': 'auto_mode_heater',
                     'name': 'Priorytet grzałki',
                     'active': False,
                     'check_schedule': False},
                ]),
                schedules_types.insert().values([
                    {'id': 'low_power_cost'},
                    {'id': 'water_heater'}
                ]),
                smart_devices.insert().values(
                    [{'name': 'water_heater',
                      'device_id': '70050308600194b8cb32',
                      'ip_address': '192.168.1.26',
                      'local_key': 'a5dac5e5d5c4f941',
                      'version': 3.1
                      },
                     {'name': 'window_bulb',
                      'device_id': '115180622462ab51fad2',
                      'ip_address': '192.168.1.30',
                      'local_key': 'c888164e5b6697d1',
                      'version': 3.3
                      },
                     {'name': 'valve',
                      'device_id': 'bf80954079eb5cce8c7tlt',
                      'ip_address': '192.168.1.34',
                      'local_key': 'e4d05d3a39205d0b',
                      'version': 3.3
                      },
                     {'name': 'bed_light',
                      'device_id': '115180622462ab51f1d6',
                      'ip_address': '192.168.1.29',
                      'local_key': '1923b2570707e12a',
                      'version': 3.3
                      }]
                )]

            for q in queries:
                connection.execute(q)

    def get_temp(self) -> TempConfig:
        with self.engine.begin() as connection:
            max_water_temp_query = temp_config \
                .select() \
                .where(temp_config.c.config_name == 'max_water_temp')

            max_water_temp_result = connection.execute(max_water_temp_query).fetchone()

            water_temp_query = temp_config \
                .select() \
                .where(temp_config.c.config_name == 'sensor_water')

            water_temp_result = connection.execute(water_temp_query).fetchone()

            co_temp_query = temp_config \
                .select() \
                .where(temp_config.c.config_name == 'sensor_co')

            co_temp_result = connection.execute(co_temp_query).fetchone()

        return TempConfig(
            max_water_temp=max_water_temp_result[1] if max_water_temp_result else 0,
            water_temp=water_temp_result[1] if water_temp_result else 0,
            co_temp=co_temp_result[1] if co_temp_result else 0,
        )

    def save_temp(self, sensor: TempSensor):
        with self.engine.begin() as connection:
            sensor_select = temp_config.select() \
                .where(temp_config.c.config_name == sensor.name)
            sensor_result = connection.execute(sensor_select).fetchone()
            if sensor_result:
                sensor_query = temp_config.update() \
                    .where(temp_config.c.config_name == sensor.name) \
                    .values(value=sensor.temperature)
            else:
                sensor_query = temp_config.insert().values(
                    config_name=sensor.name,
                    value=sensor.temperature
                )
            connection.execute(sensor_query)

    def get_water_heater_schedulers(self) -> List[WaterHeatSchedule]:
        result = []

        with self.engine.begin() as connection:
            schedules_query = schedules.select().where(schedules.c.schedule_type_id == 'water_heater')
            schedules_rows = connection.execute(schedules_query)
            for row in schedules_rows:
                weekdays_query = schedules_days.select().where(schedules_days.c.schedule_id == row[0])
                weekdays_rows = connection.execute(weekdays_query)
                weekdays = []
                for days in weekdays_rows:
                    weekdays.append(Weekday(days[2]))

                result_schedule = WaterHeatSchedule(
                    start=row[2],
                    end=row[3],
                    weekdays=weekdays
                )

                result.append(result_schedule)
        return result

    def get_low_cost_power_schedulers(self) -> List[LowerCostPower]:
        result = []

        with self.engine.begin() as connection:
            schedules_query = schedules.select().where(schedules.c.schedule_type_id == 'low_power_cost')
            schedules_rows = connection.execute(schedules_query)
            for row in schedules_rows:
                weekdays_query = schedules_days.select().where(schedules_days.c.schedule_id == row[0])
                weekdays_rows = connection.execute(weekdays_query)
                weekdays = []
                for days in weekdays_rows:
                    weekdays.append(Weekday(days[2]))

                result_schedule = LowerCostPower(
                    start=row[2],
                    end=row[3],
                    weekdays=weekdays
                )

                result.append(result_schedule)
        return result

    def get_active_operation_mode(self) -> Operation:
        with self.engine.begin() as connection:
            select = operation_modes.select().where(operation_modes.c.active == True)
            result = connection.execute(select).fetchone()
            return Operation(result[0]) if result else None

    def get_checking_schedule_status(self, operation: Operation) -> bool:
        with self.engine.begin() as connection:
            select = operation_modes.select().where(operation_modes.c.id == operation.name.lower())
            result = connection.execute(select).fetchone()
            return result[3] if result else False

    def add_device(self, device: Device):
        with self.engine.begin() as connection:
            insert = smart_devices.insert().values(
                name=device.name,
                device_id=device.device_id,
                ip_address=device.ip_address,
                local_key=device.local_key
            )
            connection.execute(insert)

    def get_device_by_name(self, name: str) -> Device:
        with self.engine.begin() as connection:
            select = smart_devices.select().where(smart_devices.c.name == name)
            result = connection.execute(select).fetchone()
            if result:
                return Device(
                    name=result[1],
                    device_id=result[2],
                    ip_address=result[3],
                    local_key=result[4],
                    version=result[5]
                )

    def _add_schedule(self, schedule: Schedule, schedule_type: str):
        with self.engine.begin() as connection:
            insert = schedules.insert() \
                .values(
                schedule_type_id=schedule_type,
                start_time=schedule.start,
                stop_time=schedule.end,

            ) \
                .returning(schedules.c.id)
            result = connection.execute(insert)
            schedule_new_id = result.fetchone()[0]

            for weekday in schedule.weekdays:
                schedule_day_insert = schedules_days.insert().values(
                    schedule_id=schedule_new_id,
                    weekday=weekday.value
                )
                connection.execute(schedule_day_insert)

    def add_water_heater_schedule(self, schedule: WaterHeatSchedule) -> None:
        self._add_schedule(schedule, 'water_heater')

    def add_low_cost_power_schedule(self, schedule: LowerCostPower) -> None:
        self._add_schedule(schedule, 'low_power_cost')

    def set_device_status(self, device_name: str, status: Status):
        with self.engine.begin() as connection:
            update = smart_devices.update() \
                .where(smart_devices.c.name == device_name) \
                .values(last_status=status.value)
            connection.execute(update)

    def get_device_status(self, device_name: str) -> bool:
        with self.engine.begin() as connection:
            select = smart_devices.select() \
                .where(smart_devices.c.name == device_name)
            result = connection.execute(select).fetchone()

            return result[6] if result else False

    def set_active_operation_mode(self, operation: Operation) -> None:
        with self.engine.begin() as connection:
            for o in Operation:
                connection.execute(
                    operation_modes.update() \
                        .where(operation_modes.c.id == o.value) \
                        .values(active=False)
                )

            update = operation_modes.update() \
                .where(operation_modes.c.id == operation.value) \
                .values(active=True)

            connection.execute(update)

    def set_low_cost_checking(self, operation: Operation, value: bool) -> None:
        with self.engine.begin() as connection:
            update = operation_modes.update() \
                .where(operation_modes.c.id == operation.value) \
                .values(check_schedule=value)

            connection.execute(update)

    def get_current_power(self, device_name: str) -> float:
        with self.engine.begin() as connection:
            query = temp_config \
                .select() \
                .where(temp_config.c.config_name == device_name)

            query_result = connection.execute(query).fetchone()
            return query_result[1] if query_result else 0.0

    def set_current_power(self, device_name: str, value: float) -> None:
        with self.engine.begin() as connection:
            update = temp_config.update() \
                .where(temp_config.c.config_name == device_name) \
                .values(value=value)

            connection.execute(update)

    def set_notifier_status(self, device_name: str, value: bool) -> None:
        with self.engine.begin() as connection:
            update = notifier.update().where(notifier.c.name == device_name).values(value=value)
            connection.execute(update)

    def get_notifier_status(self, device_name: str) -> bool:
        with self.engine.begin() as connection:
            select = notifier.select().where(notifier.c.name == device_name)
            result = connection.execute(select).fetchone()
            return result[1] if result else False

    def get_chats(self) -> List[str]:
        with self.engine.begin() as connection:
            select = telegram.select()
            result = connection.execute(select)
            return [item[1] for item in result]

    def get_hysteresis(self) -> Hysteresis:
        with self.engine.begin() as connection:
            select = hysteresis.select().where(hysteresis.c.id == 1)
            result = connection.execute(select).fetchone()
            return Hysteresis(
                Status(result[1]),
                result[2]
            )

    def set_hysteresis_status(self, status: Status) -> None:
        with self.engine.begin() as connection:
            update = hysteresis.update().where(hysteresis.c.id == 1).values(status=status.value)
            connection.execute(update)

    def set_hysteresis_value(self, value: int) -> None:
        with self.engine.begin() as connection:
            update = hysteresis.update().where(hysteresis.c.id == 1).values(value=value)
            connection.execute(update)
