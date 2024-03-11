import unittest
from whilte_box import VendingMachine, TrafficLight


class TestVendingMachine(unittest.TestCase):
    def setUp(self):
        """
        Set up a new VendingMachine instance before each test
        """
        self.machine = VendingMachine()

    def test_initial_state(self):
        """
        Test that the initial state is "Ready"
        """
        self.assertEqual(self.machine.state, "Ready")

    def test_insert_coin(self):
        """
        Test that inserting a coin changes the state to "Dispensing"
        """
        result = self.machine.insert_coin()
        self.assertEqual(result, "Coin Inserted. Select your drink.")
        self.assertEqual(self.machine.state, "Dispensing")

    def test_insert_coin_when_dispensing(self):
        """
        Test that inserting a coin when already dispensing returns an error
        """
        self.machine.insert_coin()  # set state to "Dispensing"
        result = self.machine.insert_coin()
        self.assertEqual(result, "Invalid operation in current state.")

    def test_select_drink(self):
        """
        Test that selecting a drink changes the state to "Ready"
        """
        self.machine.insert_coin()  # set state to "Dispensing"
        result = self.machine.select_drink()
        self.assertEqual(result, "Drink Dispensed. Thank you!")
        self.assertEqual(self.machine.state, "Ready")

    def test_select_drink_when_ready(self):
        """
        Test that selecting a drink when in "Ready" state returns an error
        """
        result = self.machine.select_drink()
        self.assertEqual(result, "Invalid operation in current state.")


class TrafficLightTest(unittest.TestCase):
    def setUp(self):
        """
        Set up a new TrafficLight instance before each test
        """
        self.light = TrafficLight()

    def test_initial_state(self):
        """
        Test that the initial state is "Red"
        """
        self.assertEqual(self.light.state, "Red")

    def test_change_state(self):
        """
        Test that changing the state changes the state to the next one
        """
        self.light.change_state()
        self.assertEqual(self.light.state, "Green")
        self.light.change_state()
        self.assertEqual(self.light.state, "Yellow")
        self.light.change_state()
        self.assertEqual(self.light.state, "Red")

    def test_change_state_when_yellow(self):
        """
        Test that changing the state when it is yellow changes the state to red
        """
        self.light.change_state()
        self.light.change_state()
        self.light.change_state()
        self.assertEqual(self.light.state, "Red")

    def test_change_state_when_red(self):
        """
        Test that changing the state when it is red changes the state to green
        """
        self.light.change_state()
        self.assertEqual(self.light.state, "Green")

    def test_change_state_when_green(self):
        """
        Test that changing the state when it is green changes the state to yellow
        """
        self.light.change_state()
        self.light.change_state()
        self.assertEqual(self.light.state, "Yellow")


if __name__ == "__main__":
    unittest.main()
