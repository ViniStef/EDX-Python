from bank import value
import pytest

def test_value():
    assert value("hello") == 0


def test_hello_upper():
    assert value("Hello,") == 0


def test_upper():
    assert value("How's it going") == 20


def test_not_h_start():
    assert value("good morning") == 100

def test_number():
    with pytest.raises(ValueError):
        value(0)

