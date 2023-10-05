from seasons import handle_date, convert_date, convert_min_words
import pytest


def test_handle_date():
    assert handle_date("2002-02-14") == "2002-02-14"
    assert handle_date("1221-09-07") == "1221-09-07"
    assert handle_date("2022-04-30") == "2022-04-30"


def test_convert_min_words():
    assert convert_min_words(3921) == "Three thousand, nine hundred twenty-one minutes."
    assert (
        convert_min_words(2123921) == "Two million, one hundred twenty-three thousand, nine hundred twenty-one minutes.")


def test_errors():
    with pytest.raises(SystemExit):
        handle_date("January 1st, 1994")
        handle_date("2002-14-02")
        handle_date("202-14-02")
        handle_date("2001-14-2")
