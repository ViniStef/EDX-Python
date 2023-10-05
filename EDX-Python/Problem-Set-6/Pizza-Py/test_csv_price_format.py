from csv_price_format import formatted_table
import pytest

def test_formatted_table():
    with pytest.raises(FileNotFoundError):
        formatted_table("test.py")