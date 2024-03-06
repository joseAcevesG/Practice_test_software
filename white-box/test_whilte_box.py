import unittest
from whilte_box import (
    check_loan_eligibility,
    calculate_shipping_cost,
    grade_quiz,
    authenticate_user,
)


class TestCheckLoanEligibility(unittest.TestCase):
    def test_not_eligible(self):
        result = check_loan_eligibility(25000, 600)
        self.assertEqual(result, "Not Eligible")

    def test_standard_loan(self):
        result = check_loan_eligibility(40000, 720)
        self.assertEqual(result, "Standard Loan")

    def test_secured_loan(self):
        result = check_loan_eligibility(50000, 600)
        self.assertEqual(result, "Secured Loan")

    def test_premium_loan(self):
        result = check_loan_eligibility(70000, 800)
        self.assertEqual(result, "Premium Loan")


class TestCalculateShippingCost(unittest.TestCase):
    def test_small_package(self):
        result = calculate_shipping_cost(1, 10, 10, 10)
        self.assertEqual(result, 5)

    def test_medium_package(self):
        result = calculate_shipping_cost(3, 20, 20, 20)
        self.assertEqual(result, 10)

    def test_large_package(self):
        result = calculate_shipping_cost(10, 40, 40, 40)
        self.assertEqual(result, 20)


class TestGradeQuiz(unittest.TestCase):
    def test_pass(self):
        result = grade_quiz(8, 1)
        self.assertEqual(result, "Pass")

    def test_conditional_pass(self):
        result = grade_quiz(6, 3)
        self.assertEqual(result, "Conditional Pass")

    def test_fail(self):
        result = grade_quiz(4, 4)
        self.assertEqual(result, "Fail")


class TestAuthenticateUser(unittest.TestCase):
    def test_admin_authentication(self):
        result = authenticate_user("admin", "admin123")
        self.assertEqual(result, "Admin")

    def test_user_authentication(self):
        result = authenticate_user("john5", "password123")
        self.assertEqual(result, "User")

    def test_invalid_authentication(self):
        result = authenticate_user("user", "pass")
        self.assertEqual(result, "Invalid")


if __name__ == "__main__":
    unittest.main()
