import os
import sys
import unittest
from io import StringIO
from unittest.mock import patch

sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/../")
# flake8: noqa
from white_box_homework.white_box import (
    BankAccount,
    BankingSystem,
    DocumentEditingSystem,
    ElevatorSystem,
    Product,
    ShoppingCart,
    TrafficLight,
    UserAuthentication,
    VendingMachine,
    authenticate_user,
    calculate_items_shipping_cost,
    calculate_order_total,
    calculate_quantity_discount,
    calculate_shipping_cost,
    calculate_total_discount,
    categorize_product,
    celsius_to_fahrenheit,
    check_file_size,
    check_flight_eligibility,
    check_loan_eligibility,
    check_number_status,
    get_weather_advisory,
    grade_quiz,
    validate_credit_card,
    validate_date,
    validate_email,
    validate_login,
    validate_password,
    validate_url,
    verify_age,
)

# flake8: noqa


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
        self.assertEqual(calculate_quantity_discount(10), "5% Discount")

    def test_10_percent_discount(self):
        """Test that it returns '10% Discount' for quantity greater than 10"""
        self.assertEqual(calculate_quantity_discount(11), "10% Discount")


# 16
class TestCheckFileSize(unittest.TestCase):
    def test_valid_file_size(self):
        """Test that it correctly identifies a valid file size"""
        self.assertEqual(check_file_size(500), "Valid File Size")

    def test_invalid_file_size(self):
        """Test that it correctly identifies an invalid file size"""
        self.assertEqual(check_file_size(2000000), "Invalid File Size")
        self.assertEqual(check_file_size(-1), "Invalid File Size")

    def test_boundary_file_size(self):
        """Test that it correctly identifies the boundary file size"""
        self.assertEqual(check_file_size(1048576), "Valid File Size")
        self.assertEqual(check_file_size(0), "Valid File Size")


# 17
class TestCheckLoanEligibility(unittest.TestCase):
    def test_not_eligible(self):
        """Test that it correctly identifies when the person is not eligible for a loan"""
        self.assertEqual(check_loan_eligibility(29999, 600), "Not Eligible")

    def test_secured_loan(self):
        """Test that it correctly identifies when the person is eligible for a Secured Loan"""
        self.assertEqual(check_loan_eligibility(50000, 700), "Secured Loan")
        self.assertEqual(check_loan_eligibility(60000, 600), "Secured Loan")
        self.assertEqual(check_loan_eligibility(30000, 600), "Secured Loan")

    def test_standard_loan(self):
        """Test that it correctly identifies when the person is eligible for a secured loan"""
        self.assertEqual(check_loan_eligibility(50000, 701), "Standard Loan")
        self.assertEqual(check_loan_eligibility(60000, 740), "Standard Loan")
        self.assertEqual(check_loan_eligibility(30000, 740), "Standard Loan")

    def test_premium_loan(self):
        """Test that it correctly identifies when the person is eligible for a premium loan"""
        self.assertEqual(check_loan_eligibility(60001, 800), "Premium Loan")
        self.assertEqual(check_loan_eligibility(70000, 751), "Premium Loan")

    def test_standard_loan_boundary(self):
        """Test that it correctly identifies when the person is eligible for a standard loan at the income boundary"""
        self.assertEqual(check_loan_eligibility(70000, 750), "Standard Loan")
        self.assertEqual(check_loan_eligibility(60001, 700), "Standard Loan")


# 18
class TestCalculateShippingCost(unittest.TestCase):
    def test_small_package(self):
        """Test that it correctly calculates the shipping cost for a small package"""
        weight = 1
        length = 10
        width = 10
        height = 10
        self.assertEqual(calculate_shipping_cost(weight, length, width, height), 5)

    def test_medium_package(self):
        """Test that it correctly calculates the shipping cost for a medium package"""
        weight = 2
        length = 11
        width = 11
        height = 11
        self.assertEqual(calculate_shipping_cost(weight, length, width, height), 10)
        weight = 5
        length = 30
        width = 30
        height = 30
        self.assertEqual(calculate_shipping_cost(weight, length, width, height), 10)

    def test_large_package(self):
        """Test that it correctly calculates the shipping cost for a large package"""
        weight = 6
        length = 31
        width = 31
        height = 31
        self.assertEqual(calculate_shipping_cost(weight, length, width, height), 20)


# 19
class TestGradeQuiz(unittest.TestCase):
    def test_pass(self):
        """Test that it correctly grades the quiz as 'Pass'"""
        self.assertEqual(grade_quiz(7, 1), "Pass")
        self.assertEqual(grade_quiz(8, 2), "Pass")

    def test_conditional_pass(self):
        """Test that it correctly grades the quiz as 'Conditional Pass'"""
        self.assertEqual(grade_quiz(6, 3), "Conditional Pass")
        self.assertEqual(grade_quiz(5, 2), "Conditional Pass")

    def test_fail(self):
        """Test that it correctly grades the quiz as 'Fail'"""
        self.assertEqual(grade_quiz(4, 5), "Fail")
        self.assertEqual(grade_quiz(2, 4), "Fail")


# 20
class TestAuthenticateUser(unittest.TestCase):
    def test_admin_credentials(self):
        """Test that it correctly authenticates admin credentials"""
        self.assertEqual(authenticate_user("admin", "admin123"), "Admin")

    def test_valid_user_credentials(self):
        """Test that it correctly authenticates valid user credentials"""
        self.assertEqual(authenticate_user("john123", "password123"), "User")

    def test_invalid_username_length(self):
        """Test that it correctly identifies an invalid username due to length"""
        self.assertEqual(
            authenticate_user("john", "password123"),
            "Invalid",
        )

    def test_invalid_password_length(self):
        """Test that it correctly identifies an invalid password due to length"""
        self.assertEqual(authenticate_user("johndoe", "pass"), "Invalid")


# 21
class TestGetWeatherAdvisory(unittest.TestCase):
    def test_high_temperature_and_humidity(self):
        """Test for high temperature and humidity"""
        self.assertEqual(
            get_weather_advisory(31, 80),
            "High Temperature and Humidity. Stay Hydrated.",
        )
        self.assertEqual(
            get_weather_advisory(40, 71),
            "High Temperature and Humidity. Stay Hydrated.",
        )

    def test_low_temperature(self):
        """Test for low temperature"""
        self.assertEqual(get_weather_advisory(-1, 60), "Low Temperature. Bundle Up!")

    def test_no_specific_advisory(self):
        """Test for no specific advisory"""
        self.assertEqual(get_weather_advisory(0, 50), "No Specific Advisory")
        self.assertEqual(get_weather_advisory(30, 50), "No Specific Advisory")
        self.assertEqual(get_weather_advisory(60, 70), "No Specific Advisory")


# 22
class TestVendingMachine(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.vending_machine = VendingMachine()

    def setUp(self):
        self.vending_machine.state = "Ready"

    def test_initial_state(self):
        """Test that the vending machine is initially in the 'Ready' state"""
        vending_machine = VendingMachine()
        self.assertEqual(vending_machine.state, "Ready")

    def test_insert_coin(self):
        """Test inserting a coin in the vending machine"""
        result = self.vending_machine.insert_coin()
        self.assertEqual(result, "Coin Inserted. Select your drink.")

    def test_insert_coin_invalid_state(self):
        """Test inserting a coin in an invalid state"""
        self.vending_machine.state = "Dispensing"
        result = self.vending_machine.insert_coin()
        self.assertEqual(result, "Invalid operation in current state.")

    def test_select_drink(self):
        """Test selecting a drink from the vending machine"""
        self.vending_machine.state = "Dispensing"
        result = self.vending_machine.select_drink()
        self.assertEqual(result, "Drink Dispensed. Thank you!")

    def test_select_drink_invalid_state(self):
        """Test selecting a drink in an invalid state"""
        result = self.vending_machine.select_drink()
        self.assertEqual(result, "Invalid operation in current state.")


# 23
class TestTrafficLight(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.traffic_light = TrafficLight()

    def setUp(self):
        self.traffic_light.state = "Red"

    def test_initial_state(self):
        """Test that the traffic light is initially in the 'Red' state"""
        traffic_light = TrafficLight()
        self.assertEqual(traffic_light.get_current_state(), "Red")

    def test_change_state(self):
        """Test that the traffic light changes state correctly"""

        # Test changing from 'Red' to 'Green'
        self.traffic_light.change_state()
        self.assertEqual(self.traffic_light.get_current_state(), "Green")

        # Test changing from 'Green' to 'Yellow'
        self.traffic_light.change_state()
        self.assertEqual(self.traffic_light.get_current_state(), "Yellow")

        # Test changing from 'Yellow' to 'Red'
        self.traffic_light.change_state()
        self.assertEqual(self.traffic_light.get_current_state(), "Red")


# 24
class TestUserAuthentication(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.auth = UserAuthentication()

    def setUp(self):
        self.auth.state = "Logged Out"

    def initial_state(self):
        """Test that the user authentication is initially in the 'Logged Out' state"""
        auth = UserAuthentication()
        self.assertEqual(auth.state, "Logged Out")

    def test_login(self):
        """Test that the user can log in successfully"""
        self.assertEqual(self.auth.login(), "Login successful")
        self.assertEqual(self.auth.state, "Logged In")

    def test_login_invalid_state(self):
        """Test that the user cannot log in when already logged in"""
        self.auth.login()
        self.assertEqual(self.auth.login(), "Invalid operation in current state")
        self.assertEqual(self.auth.state, "Logged In")

    def test_logout(self):
        """Test that the user can log out successfully"""
        self.auth.login()
        self.assertEqual(self.auth.logout(), "Logout successful")
        self.assertEqual(self.auth.state, "Logged Out")

    def test_logout_invalid_state(self):
        self.assertEqual(self.auth.logout(), "Invalid operation in current state")
        self.assertEqual(self.auth.state, "Logged Out")


# 25
class TestDocumentEditingSystem(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.doc_sys = DocumentEditingSystem()

    def setUp(self):
        self.doc_sys.state = "Editing"

    def test_initial_state(self):
        """Test that the document editing system is initially in the 'Editing' state"""
        doc_sys = DocumentEditingSystem()
        self.assertEqual(doc_sys.state, "Editing")

    def test_save_document(self):
        self.assertEqual(self.doc_sys.save_document(), "Document saved successfully")
        self.assertEqual(self.doc_sys.state, "Saved")

    def test_edit_document(self):
        self.doc_sys.save_document()
        self.assertEqual(self.doc_sys.edit_document(), "Editing resumed")
        self.assertEqual(self.doc_sys.state, "Editing")

    def test_invalid_operation_in_editing_state(self):
        self.assertEqual(
            self.doc_sys.edit_document(), "Invalid operation in current state"
        )
        self.assertEqual(self.doc_sys.state, "Editing")

    def test_invalid_operation_in_saved_state(self):
        self.doc_sys.save_document()
        self.assertEqual(
            self.doc_sys.save_document(), "Invalid operation in current state"
        )
        self.assertEqual(self.doc_sys.state, "Saved")


# 26
class TestElevatorSystem(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.elevator = ElevatorSystem()

    def setUp(self):
        self.elevator.state = "Idle"

    def test_initial_state(self):
        """Test that the elevator system is initially in the 'Idle' state"""
        elevator = ElevatorSystem()
        self.assertEqual(elevator.state, "Idle")

    def test_move_up(self):
        """Test that the elevator moves up successfully"""
        self.assertEqual(self.elevator.move_up(), "Elevator moving up")
        self.assertEqual(self.elevator.state, "Moving Up")

    def test_move_down(self):
        """Test that the elevator moves down successfully"""
        self.assertEqual(self.elevator.move_down(), "Elevator moving down")
        self.assertEqual(self.elevator.state, "Moving Down")

    def test_stop(self):
        """Test that the elevator stops successfully"""
        self.elevator.move_up()
        self.assertEqual(self.elevator.stop(), "Elevator stopped")
        self.assertEqual(self.elevator.state, "Idle")

    def test_invalid_operation_move_up(self):
        """Test that an invalid operation is not allowed in the current state"""
        self.elevator.move_up()
        self.assertEqual(self.elevator.move_up(), "Invalid operation in current state")
        self.assertEqual(self.elevator.state, "Moving Up")
        self.assertEqual(
            self.elevator.move_down(), "Invalid operation in current state"
        )
        self.assertEqual(self.elevator.state, "Moving Up")

    def test_invalid_operation_move_down(self):
        """Test that an invalid operation is not allowed in the current state"""
        self.elevator.move_down()
        self.assertEqual(
            self.elevator.move_down(), "Invalid operation in current state"
        )
        self.assertEqual(self.elevator.state, "Moving Down")
        self.assertEqual(self.elevator.move_up(), "Invalid operation in current state")
        self.assertEqual(self.elevator.state, "Moving Down")

    def test_invalid_operation_stop(self):
        """Test that an invalid operation is not allowed in the current state"""
        self.assertEqual(self.elevator.stop(), "Invalid operation in current state")
        self.assertEqual(self.elevator.state, "Idle")


# 27
class TestBankAccount(unittest.TestCase):
    def setUp(self):
        self.account = BankAccount("1234567890", 1000)

    def test_view_account(self):
        """Test that it correctly displays the account details"""
        expected_output = "The account 1234567890 has a balance of 1000"
        self.assertEqual(self.account.view_account(), expected_output)


class TestBankingSystem(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.banking_system = BankingSystem()

    def setUp(self):
        self.banking_system.logged_in_users.clear()

    @patch("sys.stdout", new_callable=StringIO)
    def test_authenticate_valid_credentials(self, mock_stdout):
        """Test that it correctly authenticates a user with valid credentials"""
        self.assertTrue(self.banking_system.authenticate("user123", "pass123"))
        self.assertEqual(
            mock_stdout.getvalue().strip(),
            "User user123 authenticated successfully.",
        )

    @patch("sys.stdout", new_callable=StringIO)
    def test_authenticate_invalid_username(self, mock_stdout):
        """Test that it correctly handles authentication failure with an invalid username"""
        self.assertFalse(self.banking_system.authenticate("invalid_user", "pass123"))
        self.assertEqual(mock_stdout.getvalue().strip(), "Authentication failed.")

    @patch("sys.stdout", new_callable=StringIO)
    def test_authenticate_invalid_password(self, mock_stdout):
        """Test that it correctly handles authentication failure with an invalid password"""
        self.assertFalse(self.banking_system.authenticate("user123", "invalid_pass"))
        self.assertEqual(mock_stdout.getvalue().strip(), "Authentication failed.")

    @patch("sys.stdout", new_callable=StringIO)
    def test_authenticate_already_logged_in(self, mock_stdout):
        """Test that it correctly handles authentication failure when the user is already logged in"""
        self.banking_system.authenticate("user123", "pass123")
        self.assertFalse(self.banking_system.authenticate("user123", "pass123"))
        output_lines = mock_stdout.getvalue().strip().split("\n")
        second_print_output = output_lines[1]
        self.assertEqual(second_print_output, "User already logged in.")

    @patch("sys.stdout", new_callable=StringIO)
    def test_transfer_money_not_logged_in(self, mock_stdout):
        """Test that it correctly handles a money transfer when the user is not logged in"""
        self.assertFalse(
            self.banking_system.transfer_money("user123", "receiver", 100, "regular")
        )
        self.assertEqual(mock_stdout.getvalue().strip(), "Sender not authenticated.")

    def test_transfer_money_regular_transaction(self):
        """Test that it correctly processes a regular money transfer"""
        self.banking_system.authenticate("user123", "pass123")
        self.assertTrue(
            self.banking_system.transfer_money("user123", "receiver", 100, "regular")
        )

    def test_transfer_money_express_transaction(self):
        """Test that it correctly processes an express money transfer"""
        self.banking_system.authenticate("user123", "pass123")
        self.assertTrue(
            self.banking_system.transfer_money("user123", "receiver", 100, "express")
        )

    def test_transfer_money_scheduled_transaction(self):
        """Test that it correctly processes a scheduled money transfer"""
        self.banking_system.authenticate("user123", "pass123")
        self.assertTrue(
            self.banking_system.transfer_money("user123", "receiver", 100, "scheduled")
        )

    @patch("sys.stdout", new_callable=StringIO)
    def test_transfer_money_invalid_transaction_type(self, mock_stdout):
        """Test that it correctly handles an invalid transaction type"""
        self.banking_system.authenticate("user123", "pass123")
        self.assertFalse(
            self.banking_system.transfer_money("user123", "receiver", 100, "invalid")
        )
        output_lines = mock_stdout.getvalue().strip().split("\n")
        second_print_output = output_lines[1]
        self.assertEqual(second_print_output, "Invalid transaction type.")

    @patch("sys.stdout", new_callable=StringIO)
    def test_transfer_money_insufficient_funds(self, mock_stdout):
        """Test that it correctly handles insufficient funds for a money transfer"""
        self.banking_system.authenticate("user123", "pass123")
        self.assertFalse(
            self.banking_system.transfer_money("user123", "receiver", 10000, "regular")
        )
        output_lines = mock_stdout.getvalue().strip().split("\n")
        second_print_output = output_lines[1]
        self.assertEqual(second_print_output, "Insufficient funds.")


# 28
class TestShoppingCart(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.cart = ShoppingCart()
        cls.product = Product("Product A", 10)

    def setUp(self):
        self.cart.items.clear()

    def test_add_product(self):
        self.cart.add_product(self.product, 2)
        self.assertEqual(len(self.cart.items), 1)

    def test_add_existing_product(self):
        self.cart.add_product(self.product, 2)
        self.cart.add_product(self.product, 3)
        self.assertEqual(len(self.cart.items), 1)
        self.assertEqual(self.cart.items[0]["quantity"], 5)

    def test_remove_product(self):
        self.cart.add_product(self.product, 2)
        self.cart.remove_product(self.product, 1)
        self.assertEqual(len(self.cart.items), 1)
        self.assertEqual(self.cart.items[0]["quantity"], 1)

    def test_remove_product_full_quantity(self):
        self.cart.add_product(self.product, 2)
        self.cart.remove_product(self.product, 2)
        self.assertEqual(len(self.cart.items), 0)

    @patch("sys.stdout", new_callable=StringIO)
    def test_view_cart(self, mock_stdout):
        self.cart.add_product(self.product, 2)
        expected_output = "2 x Product A - $20\n"

        self.cart.view_cart()

        self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_checkout(self):
        self.cart.add_product(self.product, 2)
        self.assertEqual(self.cart.checkout(), 20)


if __name__ == "__main__":
    unittest.main()
