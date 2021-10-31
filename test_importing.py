from testing import *

def test_ans():
    assert func(3)==5
def test_ans1():
    assert func(4)==5

def test_ans2():
    assert func(4)==5

def test_prime():
    assert prime(5)=='Prime'

def test_prime2():
    assert prime(8)=='Not Prime'

def test_odd():
    assert odd(2)=='Odd'

def test_odd2():
    assert odd(3)=='Even'

def test_sqroot():
    assert sqroot(5)==25

