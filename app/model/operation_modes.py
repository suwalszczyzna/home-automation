from datetime import datetime

from app.adapters.device_events import DeviceEvents
from app.model.devices import WaterHeater, CoilValve
from app import config
from app.model.schedulers import LowerCostPower


class AutoMode:
    def __init__(self, lower_cost_power: LowerCostPower):
        self.max_water_temp = config.max_water_temp
        self.device_events = DeviceEvents()
        self.water_heater = WaterHeater()
        self.coil_valve = CoilValve()
        self.low_cost_power = lower_cost_power
        self.check_schedule = False

    def invoke(self, water_temp: float, co_temp: float):

        if water_temp > self.max_water_temp:
            self.device_events.turn_off(self.coil_valve)
            self.device_events.turn_off(self.water_heater)
        else:
            if water_temp < co_temp:
                self.device_events.turn_on(self.coil_valve)
                self.device_events.turn_off(self.water_heater)
            elif water_temp >= co_temp:
                self.device_events.turn_off(self.coil_valve)
                self.heater_turn_on()

    def heater_turn_on(self):
        is_lower_cost = self.low_cost_power.in_schedule(datetime.now())
        if self.check_schedule and is_lower_cost:
            self.device_events.turn_on(self.water_heater)
        else:
            self.device_events.turn_off(self.water_heater)
