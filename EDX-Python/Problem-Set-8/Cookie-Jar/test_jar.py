from jar import Jar
import pytest

def test_init():
    jar = Jar(28)
    jar.deposit(25)
    print(jar._capacity)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"
    jar.withdraw(25)
    assert str(jar) == ""

def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar()
    with pytest.raises(ValueError):
        jar.deposit(15)
    jar.deposit(8)
    assert jar.size == 8


def test_withdraw():
    jar = Jar()
    with pytest.raises(ValueError):
        jar.withdraw(2)
    jar.deposit(7)
    with pytest.raises(ValueError):
        jar.withdraw(8)
    jar.withdraw(6)
    assert str(jar) == "🍪"


def test_capacity():
    jar = Jar()
    jar.capacity = 20
    jar.deposit(19)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


