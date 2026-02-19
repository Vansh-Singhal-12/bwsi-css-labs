"""
tests_1b.py

This module contains unit tests for the simple_calculator function defined in lab_1b.py.
"""

import pytest
from labs.lab_1.lab_1b import simple_calculator

def test_addition():
    assert simple_calculator("add", 5, 3) == 8          
    assert simple_calculator("add", -2, 2) == 0         
    assert simple_calculator("add", 0, 0) == 0        

def test_subtraction():
    assert simple_calculator("subtract", 5, 3) == 2     
    assert simple_calculator("subtract", -2, -2) == 0   
    assert simple_calculator("subtract", 0, 5) == -5    

def test_multiplication():
    assert simple_calculator("multiply", 5, 3) == 15    
    assert simple_calculator("multiply", -2, 2) == -4  
    assert simple_calculator("multiply", 0, 100) == 0   

def test_division():
    assert simple_calculator("divide", 6, 3) == 2       
    assert simple_calculator("divide", -4, 2) == -2     
    assert simple_calculator("divide", 5, 2) == 2.5   

def test_division_by_zero():
    with pytest.raises(ValueError, match="Cannot divide by zero."):
        simple_calculator("divide", 5, 0)               # Test division by zero

def test_invalid_operation():
    with pytest.raises(ValueError, match="Invalid " \
    "operation. " \
    "Please choose from 'add', " \
    "'subtract', 'multiply', or 'divide'."):
        simple_calculator("modulus", 5, 3)              # Test for invalid operation
    with pytest.raises(ValueError, match="Invalid" \
    " operation. Please choose from 'add', " \
    "'subtract', 'multiply', or 'divide'."):
        simple_calculator("", 5, 3)                     # Test for empty operation

if __name__ == "__main__":
    pytest.main()

def test_more_math():
    # Standard input
    assert simple_calculator("add", 100, 200) == 300
    
    # Negative number edge case
    assert simple_calculator("subtract", -5, -5) == 0
    
    # Decimal/Float edge case
    assert simple_calculator("multiply", 2.5, 2) == 5.0