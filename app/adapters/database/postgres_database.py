import uuid
from typing import List
from sqlalchemy import create_engine, MetaData, Column, Table, Text, Float, DateTime, Time, func, ForeignKey, Integer, Boolean
from sqlalchemy.dialects.postgresql import UUID

from app.domain.abstract_database import AbstractDatabase
from app.domain.devices import Device
from app.domain.operation_modes import Operation, TempConfig
from app.domain.schedulers import LowerCostPower, WaterHeatSchedule

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
            water_temp_query = temp_history\
                .select()\
                .where(temp_history.c.sensor == 'sensor_water')

    def get_water_heater_schedulers(self) -> List[WaterHeatSchedule]:
        pass

    def get_low_cost_power_schedulers(self) -> List[LowerCostPower]:
        pass

    def get_active_operation_mode(self) -> Operation:
        pass

    def get_device_by_name(self, name: str) -> Device:
        pass
