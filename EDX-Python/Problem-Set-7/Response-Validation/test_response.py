import pytest
from response import check_email
from validator_collection import errors

def test_check_email():
    assert check_email("malan@harvard.edu") == "Valid"
    assert check_email("viniciussteflitsch@gmail.com") == "Valid"
    assert check_email("malan@@@harvard.edu") == "Invalid"
    assert check_email("viniciussteflitsch@gmail..com") == "Invalid"
    assert check_email("malan@harvard") == "Invalid"
    assert check_email("malanharvard.edu") == "Invalid"
    assert check_email("malan@har*vard.edu") == "Invalid"
    assert check_email("malan@har*vard,edu") == "Invalid"

def test_errors():
    with pytest.raises(ValueError):
        check_email("this-is-an-invalid-email")
    with pytest.raises(errors.EmptyValueError):
        check_email(None)
    with pytest.raises(errors.InvalidEmailError):
        check_email("invalid@invalid")