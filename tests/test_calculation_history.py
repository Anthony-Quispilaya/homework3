from decimal import Decimal
import pytest

from calculator.calculation_class import calculation_class
from calculator.calculation_history import HistoryCalc

from calculator.arithmetic_operations import add, subtract
@pytest.fixture
def setup_calculations():
    '''This function will clear the entire calculation history
    and create a sample calculation as a test'''
    HistoryCalc.clear_history()
    HistoryCalc.add_calculation(calculation_class(Decimal('10'), Decimal('5'), add))
    # Performing addition test first
    HistoryCalc.add_calculation(calculation_class(Decimal('20'), Decimal('3'), subtract))
    # Performing multiplication test second'''
    
def test_add_calculation(setup_calculations):
    '''Test adding a calculation to the history'''
    # Created new cal variable with information stored
    calc = calculation_class(Decimal('2'), Decimal('2'), add)
    # Add muliplication calculation to history list
    HistoryCalc.add_calculation(calc)
    # Assert the calculation was added to the history
    assert HistoryCalc.get_latest_history() == calc, "Failed to add the calculation to the history list"
    
def test_retrieve_history(setup_calculations):
    '''Test the retrieve history function'''
    # Store retrieved history into history var
    history = HistoryCalc.retrieve_history()
    # Assert that the history contains 2 calculations, must match
    # the setup_calculations function calculations
    assert len(history) == 2, "History does not contain the expected number of calculations"
    
def test_clear_history(setup_calculations):
    '''Test the clear history function'''
    HistoryCalc.clear_history()
    assert len(HistoryCalc.retrieve_history()) == 0, "History was not cleared"

def test_get_latest_history(setup_calculations):
    '''Test getting the latest history function'''
    # Store latest history calculation into latest var
    latest = HistoryCalc.get_latest_history()
    # Assert the latest calculation matches the expected values
    assert latest.a == Decimal('20') and latest.b == Decimal('3'), "Did not get the correct calculation"
    
def test_find_by_arithmetic_operation(setup_calculations):
    '''Test finding calculation in history by arithmetic operation type'''
    
    add_operations = HistoryCalc.find_by_arithmetic_operation("add")
    assert len(add_operations) == 1, "Did not find the correct number of calculation with add operation"
    
    subtract_operations = HistoryCalc.find_by_arithmetic_operation("subtract")
    assert len(subtract_operations) == 1, "Did not find the correct number of calculation with multiply operation"

def test_get_latest_with_empty_history():
    """Test getting the latest calculation when the history is empty."""
    # Ensure the history is empty by clearing it.
    HistoryCalc.clear_history()
    # Assert that the latest calculation is None since the history is empty.
    assert HistoryCalc.get_latest_history() is None, "Expected None for latest calculation with empty history"

    