import unittest
from unittest import mock

from src.timer import perform_action_based_on_time


class TimerTestCase(unittest.TestCase):
    def test_perform_action_based_on_time_action_a(self):
        with mock.patch("time.time", return_value=5):
            result = perform_action_based_on_time()
            self.assertEqual(result, "Action A")

    def test_perform_action_based_on_time_action_b(self):
        with mock.patch("time.time", return_value=15):
            result = perform_action_based_on_time()
            self.assertEqual(result, "Action B")


if __name__ == "__main__":
    unittest.main()
