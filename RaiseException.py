import pytest


def myfunc():
    raise ValueError("Exception 123 raised")


def test_match():
    with pytest.raises(ValueError, match=r".* 123 .*"):
        myfunc()

def test_match2():
    with pytest.raises(ValueError, match=r".* 0 .*"):
        myfunc()
    