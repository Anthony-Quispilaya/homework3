'''My Calculator Test'''
from decimal import Decimal
import pytest
from calculator.calculation_history import calculation_class
from calculator.arithmetic_operations import add, subtract, mulitply, divide

def test_addition():
    '''Addition function test'''
    calculation = calculation_class(Decimal('20'), Decimal('5'), add)
    assert calculation.perform() == Decimal('25'), "Addition test failed"

def test_subtraction():
    '''Subtraction function test'''
    calculation = calculation_class(Decimal('5'), Decimal('1'), subtract)
    assert calculation.perform() == Decimal('4'), "Subtraction test failed"

def test_multiplication():
    '''Multiplication function test'''
    calculation = calculation_class(Decimal('4'), Decimal('3'), mulitply)
    assert calculation.perform() == Decimal('12'), "Multiplication test failed"

def test_division():
    '''Division function test'''
    calculation = calculation_class(Decimal('10'), Decimal('2'), divide)
    assert  calculation.perform() == Decimal('5'), "Division test failed"

def test_divide_by_zero():
    '''Testing the divide by zero exception'''
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        calculation = calculation_class(Decimal('20'), Decimal('0'), divide)
        calculation.perform()
