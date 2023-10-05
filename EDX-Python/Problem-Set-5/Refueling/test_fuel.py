from fuel import convert,gauge
import pytest

def test_convert():
    assert convert("10/2") == "Please enter a valid fuel fraction." 
    assert convert("1/8") == 12
    assert convert("49/100") == 49
    assert convert("1/0") == None
    assert convert("w/2") == None

def test_gauge():
    assert gauge(40) == "40%"
    assert gauge(99) == "F"
    assert gauge(0) == "E"
    assert gauge(98) == "98%"
