'''My Calculator Test'''
from calculator.arithmetic_operations import add, subtract, mulitply, divide

def test_addition():
    '''Addition function test'''    
    assert add(2,2) == 4

def test_subtraction():
    '''Subtraction function test'''    
    assert subtract(2,2) == 0

def test_multiplication():
    '''Multiplication function test'''
    assert mulitply(5,2) == 10

def test_division():
    '''Division function test'''
    assert divide(10,2) == 5
