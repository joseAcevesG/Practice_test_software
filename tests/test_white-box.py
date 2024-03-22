import os
import sys
import unittest

print(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/../")
from white_box_homework.white_box import (
    calculate_items_shipping_cost,
    calculate_order_total,
    calculate_quantity_discount,
    calculate_total_discount,
    categorize_product,
    celsius_to_fahrenheit,
    check_flight_eligibility,
    check_number_status,
    validate_credit_card,
    validate_date,
    validate_email,
    validate_login,
    validate_password,
    validate_url,
    verify_age,
)


# 1
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


# 2
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


# 3
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


# 4
class TestCalculateOrderTotal(unittest.TestCase):
    def test_single_item_no_discount(self):
        items = [{"quantity": 1, "price": 10}]
        self.assertEqual(calculate_order_total(items), 10)

    def test_single_item_with_basic_discount(self):
        items = [{"quantity": 7, "price": 10}]
        self.assertEqual(calculate_order_total(items), 66.5)

    def test_single_item_with_advanced_discount(self):
        items = [{"quantity": 11, "price": 10}]
        self.assertEqual(calculate_order_total(items), 99)

    def test_multiple_items_no_discount(self):
        items = [
            {"quantity": 2, "price": 5},
            {"quantity": 3, "price": 8},
            {"quantity": 1, "price": 3},
        ]
        self.assertEqual(calculate_order_total(items), 37)

    def test_empty_order(self):
        items = []
        self.assertEqual(calculate_order_total(items), 0)


# 5
class TestCalculateItemsShippingCost(unittest.TestCase):
    def test_standard_shipping_under_5kg(self):
        items = [{"weight": 2}, {"weight": 3}]
        shipping_cost = calculate_items_shipping_cost(items, "standard")
        self.assertEqual(shipping_cost, 10)

    def test_standard_shipping_between_5kg_and_10kg(self):
        items = [{"weight": 6}, {"weight": 4}]
        shipping_cost = calculate_items_shipping_cost(items, "standard")
        self.assertEqual(shipping_cost, 15)

    def test_standard_shipping_over_10kg(self):
        items = [{"weight": 12}, {"weight": 8}]
        shipping_cost = calculate_items_shipping_cost(items, "standard")
        self.assertEqual(shipping_cost, 20)

    def test_express_shipping_under_5kg(self):
        items = [{"weight": 2}, {"weight": 3}]
        shipping_cost = calculate_items_shipping_cost(items, "express")
        self.assertEqual(shipping_cost, 20)

    def test_express_shipping_between_5kg_and_10kg(self):
        items = [{"weight": 6}, {"weight": 4}]
        shipping_cost = calculate_items_shipping_cost(items, "express")
        self.assertEqual(shipping_cost, 30)

    def test_express_shipping_over_10kg(self):
        items = [{"weight": 12}, {"weight": 8}]
        shipping_cost = calculate_items_shipping_cost(items, "express")
        self.assertEqual(shipping_cost, 40)

    def test_invalid_shipping_method(self):
        items = [{"weight": 2}, {"weight": 3}]
        with self.assertRaises(ValueError):
            calculate_items_shipping_cost(items, "invalid")


# 6
class TestValidateLogin(unittest.TestCase):
    def test_valid_credentials(self):
        """Test that it correctly validates valid login credentials"""
        self.assertEqual(validate_login("johndoe", "password123"), "Login Successful")

    def test_invalid_username_length(self):
        """Test that it correctly identifies an invalid username due to length"""
        self.assertEqual(
            validate_login("johndoe123456789054354543643643643643643", "password123"),
            "Login Failed",
        )

    def test_invalid_password_length(self):
        """Test that it correctly identifies an invalid password due to length"""
        self.assertEqual(validate_login("johndoe", "pass"), "Login Failed")

    def test_invalid_credentials(self):
        """Test that it correctly identifies invalid login credentials"""
        self.assertEqual(
            validate_login("johndoe", "wrongpassword63464365634653634643643"),
            "Login Failed",
        )


# 7
class TestVerifyAge(unittest.TestCase):

    def test_eligible_age(self):
        # Test lower boundary
        self.assertEqual(verify_age(18), "Eligible")
        # Test upper boundary
        self.assertEqual(verify_age(65), "Eligible")
        # Test age within the range
        self.assertEqual(verify_age(30), "Eligible")

    def test_not_eligible_age(self):
        # Test age just below the lower boundary
        self.assertEqual(verify_age(17), "Not Eligible")
        # Test age just above the upper boundary
        self.assertEqual(verify_age(66), "Not Eligible")
        # Test very young age
        self.assertEqual(verify_age(5), "Not Eligible")
        # Test very old age
        self.assertEqual(verify_age(100), "Not Eligible")

    def test_negative_age(self):
        # Test negative age
        self.assertEqual(verify_age(-5), "Not Eligible")


# 8
class TestCategorizeProduct(unittest.TestCase):

    def test_category_a(self):
        self.assertEqual(categorize_product(10), "Category A")
        self.assertEqual(categorize_product(50), "Category A")

    def test_category_b(self):
        self.assertEqual(categorize_product(51), "Category B")
        self.assertEqual(categorize_product(100), "Category B")

    def test_category_c(self):
        self.assertEqual(categorize_product(101), "Category C")
        self.assertEqual(categorize_product(200), "Category C")

    def test_category_d(self):
        self.assertEqual(categorize_product(201), "Category D")


# 9
class TestValidateEmail(unittest.TestCase):

    def test_valid_email(self):
        self.assertEqual(validate_email("test@example.com"), "Valid Email")
        self.assertEqual(validate_email("a" * 46 + "@b.d"), "Valid Email")

    def test_invalid_email(self):
        self.assertEqual(validate_email("test"), "Invalid Email")
        self.assertEqual(validate_email("test@example"), "Invalid Email")
        self.assertEqual(validate_email("a" * 47 + "@b.cd"), "Invalid Email")

    def test_edge_cases(self):
        self.assertEqual(validate_email(""), "Invalid Email")


# 10
class TestTemperatureConversion(unittest.TestCase):

    def test_celsius_to_fahrenheit(self):
        # Test lower limit
        self.assertEqual(celsius_to_fahrenheit(-100), -148)
        # Test upper limit
        self.assertEqual(celsius_to_fahrenheit(100), 212)
        # Test conversion at 0 degrees
        self.assertEqual(celsius_to_fahrenheit(0), 32)
        # Test conversion at random positive temperature
        self.assertEqual(celsius_to_fahrenheit(37), 98.6)
        # Test conversion at random negative temperature
        self.assertEqual(celsius_to_fahrenheit(-40), -40)

    def test_invalid_temperature(self):
        # Test temperature below lower limit
        self.assertEqual(celsius_to_fahrenheit(-101), "Invalid Temperature")
        # Test temperature above upper limit
        self.assertEqual(celsius_to_fahrenheit(101), "Invalid Temperature")


# 11
class TestValidateCreditCard(unittest.TestCase):

    def test_valid_card(self):
        self.assertEqual(validate_credit_card("1234567890123"), "Valid Card")
        self.assertEqual(validate_credit_card("4567890123456789"), "Valid Card")

    def test_invalid_card(self):
        self.assertEqual(validate_credit_card("12345"), "Invalid Card")
        self.assertEqual(validate_credit_card("12345678901234567"), "Invalid Card")
        self.assertEqual(validate_credit_card("1234567890abcd"), "Invalid Card")


# 12
class TestValidateDate(unittest.TestCase):

    def test_valid_date(self):
        self.assertEqual(validate_date(2022, 12, 31), "Valid Date")
        self.assertEqual(validate_date(2000, 1, 1), "Valid Date")
        self.assertEqual(validate_date(2100, 6, 15), "Valid Date")

    def test_invalid_date(self):
        self.assertEqual(validate_date(1899, 12, 31), "Invalid Date")
        self.assertEqual(validate_date(2101, 2, 30), "Invalid Date")
        self.assertEqual(validate_date(2022, 0, 1), "Invalid Date")
        self.assertEqual(validate_date(2022, 13, 1), "Invalid Date")
        self.assertEqual(validate_date(2022, 12, 32), "Invalid Date")
        self.assertEqual(validate_date(2022, 12, 0), "Invalid Date")


# 13
class TestCheckFlightEligibility(unittest.TestCase):

    def test_eligible_to_book(self):
        # Test age within the eligible range
        self.assertEqual(check_flight_eligibility(30, False), "Eligible to Book")
        # Test age at the lower boundary
        self.assertEqual(check_flight_eligibility(18, False), "Eligible to Book")
        # Test age at the upper boundary
        self.assertEqual(check_flight_eligibility(65, False), "Eligible to Book")
        # Test frequent flyer
        self.assertEqual(check_flight_eligibility(17, True), "Eligible to Book")

    def test_not_eligible_to_book(self):
        # Test age below the eligible range
        self.assertEqual(check_flight_eligibility(17, False), "Not Eligible to Book")
        # Test age above the eligible range
        self.assertEqual(check_flight_eligibility(66, False), "Not Eligible to Book")


# 14
class TestWhiteBox(unittest.TestCase):

    def test_valid_url(self):
        self.assertEqual(validate_url("http://www.example.com"), "Valid URL")
        self.assertEqual(validate_url("https://www.example.com"), "Valid URL")
        self.assertEqual(validate_url("http://example.com"), "Valid URL")
        self.assertEqual(validate_url("https://example.com"), "Valid URL")
        self.assertEqual(validate_url("http://" + "w" * 248), "Valid URL")

    def test_invalid_url(self):
        self.assertEqual(validate_url("www.example.com"), "Invalid URL")
        self.assertEqual(validate_url("example.com"), "Invalid URL")
        self.assertEqual(validate_url("http://" + "w" * 249), "Invalid URL")


# 15
class TestCalculateQuantityDiscount(unittest.TestCase):
    def test_no_discount(self):
        """Test that it returns 'No Discount' for quantity between 1 and 5"""
        self.assertEqual(calculate_quantity_discount(1), "No Discount")
        self.assertEqual(calculate_quantity_discount(5), "No Discount")

    def test_5_percent_discount(self):
        """Test that it returns '5% Discount' for quantity between 6 and 10"""
        self.assertEqual(calculate_quantity_discount(6), "5% Discount")
        self.assertEqual(calculate_quantity_discount(8), "5% Discount")
        self.assertEqual(calculate_quantity_discount(10), "5% Discount")

    def test_10_percent_discount(self):
        """Test that it returns '10% Discount' for quantity greater than 10"""
        self.assertEqual(calculate_quantity_discount(11), "10% Discount")
        self.assertEqual(calculate_quantity_discount(15), "10% Discount")
        self.assertEqual(calculate_quantity_discount(20), "10% Discount")


if __name__ == "__main__":
    unittest.main()
