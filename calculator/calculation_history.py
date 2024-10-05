from decimal import Decimal
from typing import Callable, List
from calculator.calculation_class import calculation_class

class HistoryCalc:
    history: List[calculation_class] = []
    '''Creates new list using functions from calculation_class; class'''
    
    @classmethod
    def add_history(cls, calculation: calculation_class): #cls is just like .self
        '''Add a new calculation history'''
        cls.history.append(calculation) 
    
    @classmethod
    def retrieve_history(cls) -> List[calculation_class]:
        '''Retrieve calculation history'''
        return cls.history
    
    @classmethod
    def clear_history(cls):
        '''Clear calculation history'''
        cls.history.clear()
        '''clear() is part of vscode for python'''
    
    @classmethod
    def latest_history(cls) -> calculation_class:
        '''Recover laatest calculation'''
        if cls.history:
            return cls.history[-1] # [-1] means last element in array.
        return None
    
    def find_by_arithmetic_operation(cls, operation_name: str ) -> List[calculation_class]:
        '''Return a list of calculation by arithmetic operation name'''
        return[calc for calc in cls.history if calc.ar_operation.__name__== operation_name]