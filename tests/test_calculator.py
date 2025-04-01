'''
Unit tests for calculator.py
'''

from calculator import add, subtract


def test_addition():
    assert 4 == add(2, 2)


def test_substraction():
    assert 2 == subtract(4, 2)

    

def test_multiply():
    assert 5 == multiply(4,7)

    
''' end of file '''