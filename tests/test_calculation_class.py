from decimal import Decimal
import pytest
from calculator.calculation_class import calculation_class
from calculator.arithmetic_operations import add, subtract, multiply, divide

@pytest.mark.parametrize("a, b, operation, expected", [
    (Decimal('20'), Decimal('10'), add, Decimal('30')),  # Test addition
    (Decimal('20'), Decimal('10'), subtract, Decimal('10')),  # Test subtraction
    (Decimal('20'), Decimal('10'), multiply, Decimal('200')),  # Test multiplication
    (Decimal('20'), Decimal('2'), divide, Decimal('10')),  # Test division
    (Decimal('20.5'), Decimal('5.5'), add, Decimal('26.0')),  # Test addition with decimals
    (Decimal('20.5'), Decimal('5.5'), subtract, Decimal('15.0')),  # Test subtraction with decimals
    (Decimal('20.5'), Decimal('5'), multiply, Decimal('102.5')),  # Test multiplication with decimals
    (Decimal('21.0'), Decimal('10.5'), divide, Decimal('2.0')),  # Test division with decimals
])

def test_calculation_operations(a, b, operation, expected):
    '''Test calculation operations with various scenarios'''
    # Create a Calculation instance with the provided operands and operation.
    calc = calculation_class(a, b, operation)
    # Perform the operation and assert that the result matches the expected value.
    assert calc.perform() == expected, f"Failed {operation.__name__} operation with {a} and {b}"

def test_calculation_repr():
    '''Test the string representation (__repr__) of the Calculation class'''
    # Create a Calculation instance for testing.
    calc = calculation_class(Decimal('10'), Decimal('5'), add)
    # Define the expected string representation.
    expected_repr = "Calculation(10, 5, add)"
    # Assert that the actual string representation matches the expected string.
    assert calc.__repr__() == expected_repr,"The __repr__ method output does not match the expected string."

def test_divide_by_zero():
    """
    Test division by zero to ensure it raises a ValueError.
    """
    # Create a Calculation instance with a zero divisor.
    calc = calculation_class(Decimal('10'), Decimal('0'), divide)
    # Expect a ValueError to be raised.# Attempt to perform the calculation, which should trigger the ValueError.
    with pytest.raises(ValueError, match="Cannot divide by zero"):  
        calc.perform()  
