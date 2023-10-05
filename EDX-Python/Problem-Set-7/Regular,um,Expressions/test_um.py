from um import count

def test_count():
    assert count("um, hello? how, are y- you, um, doing? um, you good?") == 3
    assert count("yummy") == 0
    assert count("um") == 1
    assert count("um?") == 1
    assert count("Um, thanks for the album.") == 1
    assert count("Um, thanks, um...") == 2


def test_different_symbols():
    assert count(" um ? you okay!!um.") == 2
    assert count("um.. how are you? *um*...") == 2
    assert count("hello! um@ hows it going?...um& thank you! um") == 3


def test_other_tests():
    assert count(" umm hey") == 0
    assert count(" umm hey um!") == 1
    assert count(" umm thats yummy yum heart") == 0
    assert count(" one means uma") == 0