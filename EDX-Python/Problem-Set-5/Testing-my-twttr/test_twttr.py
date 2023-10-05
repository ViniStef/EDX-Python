from twttr import shorten
import pytest


def main():
    test_shorten()


def test_shorten():
    assert shorten("twitter") == "twttr"

def test_capitalize():
    assert shorten("aMBER") == "MBR"
    assert shorten("ALLCAPS") == "LLCPS"

def test_number():
    with pytest.raises(ValueError):
        shorten(0)


if __name__ == "__main__":
    main()
