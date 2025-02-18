import task4
import pytest

# This function will test the discount function with only integers.
def testDiscountIntegers():
    assert task4.calculateDiscount(100, 40) == 60

# This function will test the discount function with only floats.
def testDiscountFloats():
    assert task4.calculateDiscount(129.99, 65.0) == 45.4965

# This function will test the discount function with both an integer and a float variable.
def testDiscountMixed():
    assert task4.calculateDiscount(175.10, 70) == 52.53