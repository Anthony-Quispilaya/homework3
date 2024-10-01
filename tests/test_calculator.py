'''My Calculator Test'''
from calculator.operations_basic_function import add, subtract, mulitply, divide

def test_addition():
    '''Test that addition function works '''    
    assert add(2,2) == 4

def test_subtraction():
    '''Test that addition function works '''    
    assert subtract(2,2) == 0
    
def test_multiplication():
    '''Test that the multiplication function works'''
    assert mulitply(5,2) == 10

def test_division():
    '''Test that the division funtion works'''
    assert divide(10,2) == 5