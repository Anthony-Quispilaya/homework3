from calculator.arithmetic_operations import add, subtract, mulitply, divide
from calculator.calculation_class import calculation_class
from decimal import Decimal
from typing import Callable
from calculator.calculation_history import HistoryCalc

class Calculator:
    
    
    @staticmethod
    def add(a,b):
        calculation_result = calculation_class(a, b, add)
        '''Passes the addition function from
        arithmetic_operations file'''
        return calculation_result.fetch_results()
    
    @staticmethod
    def subtract(a,b):
        calculation_result = calculation_class(a, b, subtract)
        '''Passes the subtraction function from
        arithmetic_operations file'''
        return calculation_result.fetch_results()
    
    @staticmethod
    def multiply(a,b):
        calculation_result = calculation_class(a, b, mulitply)
        '''Passes the mulitplication function from
        arithmetic_operations file'''
        return calculation_result.fetch_results()
    
    @staticmethod
    def divide(a,b):
        calculation_result = calculation_class(a, b, divide)
        '''Passes the division function from
        arithmetic_operations file'''
        return calculation_result.fetch_results()
