import unittest
from datetime import datetime

from sternman_engine import SternmanEngine
from willoughby_engine import WilloughbyEngine
from capulet_engine import CapuletEngine
from spindler_battery import SpindlerBattery
from nubbin_battery import NubbinBattery
from carrigan_tires import CarriganTires
from octoprime_tires import OctoprimeTires

class TestSpindlerBattery(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 4)
        battery = SpindlerBattery(last_service_date, today)
        self.assertTrue(battery.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        battery = SpindlerBattery(last_service_date, today)
        self.assertFalse(battery.needs_service())

class TestNubbinBattery(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)
        battery = NubbinBattery(last_service_date, today)
        self.assertTrue(battery.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        battery = NubbinBattery(last_service_date, today)
        self.assertFalse(battery.needs_service())

class TestCapuletEngine(unittest.TestCase):

    def test_engine_should_be_serviced(self):
        current_mileage = 30001
        last_service_mileage = 0
        engine = CapuletEngine(last_service_mileage, current_mileage)
        self.assertTrue(engine.needs_service())

    def test_engine_should_not_be_serviced(self):
        current_mileage = 30000
        last_service_mileage = 0
        engine = CapuletEngine(last_service_mileage, current_mileage)
        self.assertFalse(engine.needs_service())

class TestWilloughbyEngine(unittest.TestCase):

    def test_engine_should_be_serviced(self):
        current_mileage = 60001
        last_service_mileage = 0
        engine = WilloughbyEngine(last_service_mileage, current_mileage)
        self.assertTrue(engine.needs_service())

    def test_engine_should_not_be_serviced(self):
        current_mileage = 60000
        last_service_mileage = 0
        engine = WilloughbyEngine(last_service_mileage, current_mileage)
        self.assertFalse(engine.needs_service())


class TestSternmanEngine(unittest.TestCase):
    def test_needs_service_true(self):
        warning_light = True
        engine = SternmanEngine(warning_light)
        self.assertTrue(engine.needs_service())

    def test_needs_service_false(self):
        warning_light = False
        engine = SternmanEngine(warning_light)
        self.assertFalse(engine.needs_service())

class TestCarriganTires(unittest.TestCase):
    def test_needs_service_true(self):
        w = [0.1, 0.9, 0.3, 0.9]
        tires = CarriganTires(w)
        self.assertTrue(tires.needs_service())

    def test_needs_service_false(self):
        w = [0.1, 0.8, 0.3, 0.6]
        tires = CarriganTires(w)
        self.assertFalse(tires.needs_service())

class TestOctoprimeTires(unittest.TestCase):
    def test_needs_service_true(self):
        w = [0.7, 0.9, 0.8, 0.9]
        tires = OctoprimeTires(w)
        self.assertTrue(tires.needs_service())

    def test_needs_service_false(self):
        w = [0.1, 0.8, 0.3, 0.6]
        tires = OctoprimeTires(w)
        self.assertFalse(tires.needs_service())

