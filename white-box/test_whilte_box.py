import unittest
from unittest.mock import patch

from whilte_box import BankAccount, ElevatorSystem


class TestElevatorSystem(unittest.TestCase):
    def test_move_up(self):
        elevator = ElevatorSystem()
        self.assertEqual(elevator.move_up(), "Elevator moving up")

    def test_move_down(self):
        elevator = ElevatorSystem()
        self.assertEqual(elevator.move_down(), "Elevator moving down")

    def test_stop(self):
        elevator = ElevatorSystem()
        elevator.move_up()
        self.assertEqual(elevator.stop(), "Elevator stopped")

    def test_invalid_operation(self):
        elevator = ElevatorSystem()
        elevator.move_up()
        self.assertEqual(elevator.move_up(), "Invalid operation in current state")


# class TestBankAccount(unittest.TestCase):
#     def test_view_account(self):
#         account = BankAccount("1234567890", "1000")
#         self.assertEqual(account.view_account(), "The account 1234567890 has a balance of 1000")


class TestBankAccount(unittest.TestCase):
    @patch("builtins.print")
    def test_view_account(self, mock_print):
        account = BankAccount("1234567890", "1000")
        account.view_account()
        mock_print.assert_called_once_with(
            "The account 1234567890 has a balance of 1000"
        )


if __name__ == "__main__":
    unittest.main()
