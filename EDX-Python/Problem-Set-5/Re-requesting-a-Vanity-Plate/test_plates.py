import plates
import pytest

def test_two_letters_start():
    assert plates.two_letters_start("2A3ESF") == False
    assert plates.two_letters_start("S8R3GD") == False
    assert plates.two_letters_start("CDCVFS") == True


def test_is_valid_length():
    assert plates.is_valid_length("A") == False
    assert plates.is_valid_length("") == False
    assert plates.is_valid_length("AA29483") == False
    assert plates.is_valid_length("AA29483234234234") == False
    assert plates.is_valid_length("AB493A") == True


def test_middle_number_check():
    assert plates.middle_number_check("BD5894") == True
    assert plates.middle_number_check("BD0894") == False
    assert plates.middle_number_check("CS50") == True
    assert plates.middle_number_check("BD3A38") == False
    assert plates.middle_number_check("BD37Z2") == False
    assert plates.middle_number_check("BD111A") == False
    

def test_number_or_letter():
    assert plates.number_or_letter("ES32;1") == False
    assert plates.number_or_letter("KA,394") == False
    assert plates.number_or_letter("FL223.") == False
    assert plates.number_or_letter("WKSE=3") == False
    assert plates.number_or_letter("WKSE33") == True