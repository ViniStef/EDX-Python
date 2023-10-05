import pytest 
from lines import line_counter

def test_line_counter():
    assert line_counter("C:/Users/Vinicius/Desktop/Codigo/class-files/students.py") == 8
    assert line_counter("C:/Users/Vinicius/Desktop/Project_Editor/Python/HTTP_connection.py") == 3
    assert line_counter("C:/Users/Vinicius/Desktop/Codigo/EDX-Python/Problem-Set-5/Re-requesting-a-Vanity-Plate/test_plates.py") == 25