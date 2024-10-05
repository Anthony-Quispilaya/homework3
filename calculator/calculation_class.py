from decimal import Decimal
from typing import Callable
from calculator.arithmetic_operations import add, subtract, mulitply, divide

class calculation_class:
    def __init__(self, a: Decimal, b: Decimal, ar_operation: Callable[[Decimal,Decimal], Decimal]):
        self.a = a
        self.b = b
        # Stores the arithmetic operation function
        self.ar_operation = ar_operation
        
    def fetch_results(self):
        # Fetches the stored arithmetic operation function with a and b
        return self.ar_operation(self.a, self.b)
    
    @staticmethod
    def create(a: Decimal, b: Decimal, ar_operation: Callable[[Decimal, Decimal], Decimal]):
        '''Creates a new calculation object'''
        return calculation_class(a, b, ar_operation)
    
    def perform(self) -> Decimal:
        '''Performs stored calculation and returns the result'''
        return self.ar_operation(self.a, self.b)
    
    def __repr__(self):
        '''Returns that calculation in a string format'''
        return f"Calculation({self.a}, {self.b}, {self.ar_operation.__name__})"