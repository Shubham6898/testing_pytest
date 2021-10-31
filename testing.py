import pytest
import math
def func(x):
    return x+1


def prime(x):
    if x ==1:
        return 'Not Prime'
    if x ==2:
        return ' Prime'
    for i in range(2,math.ceil(math.sqrt(x))+1):
        if x%i==0:
            return 'Not Prime'
    return 'Prime'

def odd(x):
    if x%2!=0:
        return 'Odd'
    return 'Even'

def sqroot(x):
    return math.sqrt(x)


def test_ans():
    assert func(3)==5


def test_ans1():
    assert func(4)==5

def test_ans2():

    assert func(4)==5