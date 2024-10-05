from calculator.arithmetic_operations import add, subtract, multiply, divide
from calculator.calculation_class import calculation_class
from decimal import Decimal
from typing import Callable
from calculator.calculation_history import HistoryCalc

class Calculator:
    
    @staticmethod
    def perform_arithmetic_operation(a: Decimal, b: Decimal, operation: Callable[[Decimal, Decimal], Decimal]) -> Decimal:
        '''Create and perform a calculation, then return the result.'''
        # Create a Calculation object using the static create method, passing in operands and the operation
        calculation = calculation_class.create(a, b, operation)
        # Add the calculation to the history managed by the HistoryCalc class
        HistoryCalc.add_calculation(calculation)
        # Perform the calculation and return the result
        return calculation.perform()
    
    @staticmethod
    def add(a: Decimal, b: Decimal) -> Decimal:
        # Performs addition
        return Calculator.perform_arithmetic_operation(a, b, add)
    
    @staticmethod
    def subtract(a: Decimal, b: Decimal) -> Decimal:
        # Performs subtraction
        return Calculator.perform_arithmetic_operation(a, b, subtract)

    @staticmethod
    def multiply(a,b):
        # Performs multiplication
        return Calculator.perform_arithmetic_operation(a, b, multiply)
    
    @staticmethod
    def divide(a,b):
        # Performs division
        return Calculator.perform_arithmetic_operation(a, b, divide)
    