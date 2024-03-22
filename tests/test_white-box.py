import sys
import unittest

sys.path.append("/workspaces/Practice_test_software")
from white_box_homework.white_box import calculate_total_discount, check_number_status, validate_password

#1
class TestCheckNumberStatus(unittest.TestCase):
    def test_positive_number(self):
        """Test that it correctly identifies a positive number"""
        self.assertEqual(check_number_status(5), "Positive")

    def test_negative_number(self):
        """Test that it correctly identifies a negative number"""
        self.assertEqual(check_number_status(-5), "Negative")

    def test_zero(self):
        """Test that it correctly identifies zero"""
        self.assertEqual(check_number_status(0), "Zero")

#2
class TestValidatePassword(unittest.TestCase):
    def test_valid_password(self):
        """Test that it correctly validates a valid password"""
        self.assertTrue(validate_password("Abcdefg1!"))

    def test_invalid_password_length(self):
        """Test that it correctly identifies an invalid password due to length"""
        self.assertFalse(validate_password("Abcdefg"))

    def test_invalid_password_no_uppercase(self):
        """Test that it correctly identifies an invalid password with no uppercase letter"""
        self.assertFalse(validate_password("abcdefg1!"))

    def test_invalid_password_no_lowercase(self):
        """Test that it correctly identifies an invalid password with no lowercase letter"""
        self.assertFalse(validate_password("ABCDEFG1!"))

    def test_invalid_password_no_digit(self):
        """Test that it correctly identifies an invalid password with no digit"""
        self.assertFalse(validate_password("Abcdefg!"))

    def test_invalid_password_no_special_character(self):
        """Test that it correctly identifies an invalid password with no special character"""
        self.assertFalse(validate_password("Abcdefg1"))

#3
class TestCalculateTotalDiscount(unittest.TestCase):
    def test_discount_zero(self):
        """Test that it correctly calculates zero discount for total amount less than 100"""
        self.assertEqual(calculate_total_discount(99), 0)

    def test_discount_10_percent(self):
        """Test that it correctly calculates 10% discount for total amount between 100 and 500"""
        self.assertEqual(calculate_total_discount(200), 20)

    def test_discount_20_percent(self):
        """Test that it correctly calculates 20% discount for total amount greater than 500"""
        self.assertEqual(calculate_total_discount(1000), 200)

if __name__ == "__main__":
    unittest.main()
