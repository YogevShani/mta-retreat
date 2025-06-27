import re

def is_valid_mobile_number(number: str) -> bool:
    """
    Validates if the input string is a valid mobile number.
    Example: Israeli mobile numbers (starting with '05' and 10 digits)
    """
    pattern = r'^05\d{8}$'
    return bool(re.match(pattern, number))

def test_is_valid_mobile_number():
    assert is_valid_mobile_number('0541234567') == True
    assert is_valid_mobile_number('0529876543') == True
    assert is_valid_mobile_number('051234567') == False  # Too short
    assert is_valid_mobile_number('0612345678') == False # Invalid prefix
    assert is_valid_mobile_number('05412345678') == False # Too long
    assert is_valid_mobile_number('abc0541234') == False  # Not digits

if __name__ == "__main__":
    test_is_valid_mobile_number()
    print("All tests passed.!!!")
