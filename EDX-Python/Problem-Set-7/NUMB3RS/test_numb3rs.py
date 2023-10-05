from numb3rs import validate

def test_validate_nums():
    assert validate("127.0.3.255.") == False
    assert validate("127.0.3.255") == True
    assert validate(".127.0.3.255") == False


def test_validate_lengths():
    assert validate("127.0.255") == False
    assert validate("127.0.255.3.4") == False
    assert validate("0.1.1.1") == True


def test_validate_words():
    assert validate("dog") == False
    assert validate("dog.cat.bird.eel") == False