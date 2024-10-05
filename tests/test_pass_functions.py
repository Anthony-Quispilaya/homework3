'''My Calculator Test'''
from calculator import Calculator

def test_add():
    '''Addition function test'''
    assert Calculator.add(2,1) == 3

def test_subtract():
    '''Subtraction function test'''
    assert Calculator.subtract(2,1) == 1

def test_multiply():
    '''Multiplication function test'''
    assert Calculator.multiply(2,1) == 2

def test_divide():
    '''Division function test'''
    assert Calculator.divide(2,1) == 2
    