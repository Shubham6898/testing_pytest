import pytest

def fun(c):
    1/c
def test_zero_div():
    with pytest.raises(ZeroDivisionError):
        fun(1/0)