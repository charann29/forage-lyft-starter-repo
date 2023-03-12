from engine.battery import Battery

class TestWilloughbyEngine(unittest.TestCase):
    # existing test methods here

    def test_battery_needs_service_true(self):
        # current year is 2023 and battery was last serviced in 2020
        last_service_year = 2020
        battery = Battery(last_service_year)
        self.assertTrue(battery.needs_service())

    def test_battery_needs_service_false(self):
        # current year is 2023 and battery was last serviced in 2022
        last_service_year = 2022
        battery = Battery(last_service_year)
        self.assertFalse(battery.needs_service())
