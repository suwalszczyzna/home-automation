import uuid
from typing import List
from sqlalchemy import create_engine, MetaData, Column, Table, Text, Float, DateTime, Time, func, ForeignKey, Integer, \
    Boolean, desc
from sqlalchemy.dialects.postgresql import UUID

from app.domain.interfaces.abstract_database import AbstractDatabase
from app.domain.devices import Device
from app.domain.operation_modes import Operation, TempConfig
from app.domain.schedulers import LowerCostPower, WaterHeatSchedule, Schedule, Weekday

metadata = MetaData()

temp_config = Table('temp_config', metadata,
                    Column('config_name', Text, primary_key=True),
                    Column('value', Float, nullable=False)
                    )

temp_history = Table('temp_history', metadata,
                     Column('id', UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
                     Column('sensor', Text, nullable=False),
                     Column('temperature', Float, nullable=False),
                     Column('created', DateTime, nullable=False, server_default=func.now())
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
                      )


class PostgresDB(AbstractDatabase):
    def __init__(self, database_uri: str):
        self.engine = create_engine(database_uri)

    def get_temp(self) -> TempConfig:
        with self.engine.begin() as connection:
            max_water_temp_query = temp_config\
                .select()\
                .where(temp_config.c.config_name == 'max_water_temp')

            max_water_temp_result = connection.execute(max_water_temp_query).fetchone()

            water_temp_query = temp_history\
                .select()\
                .where(temp_history.c.sensor == 'sensor_water')\
                .order_by(desc(temp_history.c.created))\
                .limit(1)

            water_temp_result = connection.execute(water_temp_query).fetchone()

            co_temp_query = temp_history\
                .select()\
                .where(temp_history.c.sensor == 'sensor_co')\
                .order_by(desc(temp_history.c.created))\
                .limit(1)

            co_temp_result = connection.execute(co_temp_query).fetchone()

        return TempConfig(
            max_water_temp=max_water_temp_result[1] if max_water_temp_result else 0.0,
            water_temp=water_temp_result[2] if water_temp_result else 0.0,
            co_temp=co_temp_result[2] if co_temp_result else 0.0,
        )

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
                    local_key=result[4]
                )

    def _add_schedule(self, schedule: Schedule, schedule_type: str):
        with self.engine.begin() as connection:
            insert = schedules.insert()\
                .values(
                    schedule_type_id=schedule_type,
                    start_time=schedule.start,
                    stop_time=schedule.end,

                )\
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
