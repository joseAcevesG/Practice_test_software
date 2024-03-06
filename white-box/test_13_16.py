import whilte_box as white_box

#13
assert white_box.check_flight_eligibility(17,"YES") == "Eligible to Book", "test for frequent flyer fails"
assert white_box.check_flight_eligibility(17,"") == "Not Eligible to Book", "test for under 18 fails"
assert white_box.check_flight_eligibility(66,"") == "Not Eligible to Book", "test for over 65 fails"
assert white_box.check_flight_eligibility(21,"") == "Eligible to Book", "test for age between 18 and 65 fails"

#14
assert white_box.validate_url("http://www.google.com") == "Valid URL", "test for http fails"
assert white_box.validate_url("https://www.google.com") == "Valid URL", "test for https fails"
assert white_box.validate_url("https://www.google.com/this/is/a/very/long/url/that/should/fail") == "Invalid URL", "test for long url fails"
assert white_box.validate_url("http://www.google.com/this/is/a/very/long/url/that/should/fail") == "Invalid URL", "test for long url fails"
assert white_box.validate_url("/long/url/that/should/fail") == "Invalid URL", "test for not starting with http or https fails"


print("All test cases pass")
