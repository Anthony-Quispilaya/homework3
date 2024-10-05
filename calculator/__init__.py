from calculator.arithmetic_operations import add, subtract, mulitply, divide
from calculator.calculation_class import calculation_class

class Calculator:
    
    @staticmethod
    def add(a,b):
        calculation_result = calculation_class(a, b, add) # passes the addition function from arithmetic_operations file
        return calculation_result.fetch_results()
    
    @staticmethod
    def subtract(a,b):
        calculation_result = calculation_class(a, b, subtract) # passes the subtraction function from arithmetic_operations file
        return calculation_result.fetch_results()
    
    @staticmethod
    def multiply(a,b):
        calculation_result = calculation_class(a, b, mulitply) # passes the multiplication function from arithmetic_operations file
        return calculation_result.fetch_results()
    
    @staticmethod
    def divide(a,b):
        calculation_result = calculation_class(a, b, divide) # passes the division function from arithmetic_operations file
        return calculation_result.fetch_results()
