from working import convert,time_formats_handler
import pytest

def test_convert():
    assert convert("11:59 AM to 10:59 PM") == "11:59 to 22:59"
    assert convert("10:23 PM to 10:37 AM") == "22:23 to 10:37"
    assert convert("7 PM to 10:59 PM") == "19:00 to 22:59"


def test_time_formats_handler():
    assert time_formats_handler("10", "PM") == "22:00"
    assert time_formats_handler("10:30","AM") == "10:30"
    assert time_formats_handler("1:19","PM") == "13:19"


def test_random_cases():
    # Error is raised but its handled so it shows as failed here.
    with pytest.raises(ValueError):
        convert("14:29 PM to 3 AM")
    with pytest.raises(ValueError):
        convert("dog")
    