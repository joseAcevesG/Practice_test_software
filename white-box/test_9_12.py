import whilte_box as white_box

def test_validate_email():
    assert white_box.validate_email("uziel@email.com") == "Valid Email"
    return True

def test_invalid_email():
    assert white_box.validate_email("uziel.com") == "Invalid Email"
    return True

def test_celcius_to_fahrenheit():
    assert white_box.celsius_to_fahrenheit(100) == 212
    return True

def test_invalid_temperature():
    assert white_box.celsius_to_fahrenheit(101) == "Invalid Temperature"
    return True

def test_valid_credit_card():
    assert white_box.validate_credit_card("1234567890123456") == "Valid Card"
    return True

def test_invalid_credit_card():
    assert white_box.validate_credit_card("12345678901234567890") == "Invalid Card"
    return True

def test_valid_date():
    assert white_box.validate_date(2020, 12, 25) == "Valid Date"
    return True

def test_invalid_date():
    assert white_box.validate_date(2020, 13, 25) == "Invalid Date"
    return True


print("Testing valid email: ", test_validate_email())
print("Testing invalid email: ", test_invalid_email())

print("Testing valid temperature: ", test_celcius_to_fahrenheit())
print("Testing invalid temperature: ", test_invalid_temperature())

print("Testing valid credit card: ", test_valid_credit_card())
print("Testing invalid credit card: ", test_invalid_credit_card())

print("Testing valid date: ", test_valid_date())
print("Testing invalid date: ", test_invalid_date())
