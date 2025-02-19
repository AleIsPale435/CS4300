import pytest

# This function will take in a price and a discount amount and calculate the discounted price.
def calculateDiscount(price, discount):

    # Variables and calculates the discount from the original price entered.
    discount = discount / 100
    discountedPrice = price - (price * discount)
    return discountedPrice

# This function will test the discount function with only integers.
def testDiscountIntegers():
    assert calculateDiscount(100, 40) == 60

# This function will test the discount function with only floats.
def testDiscountFloats():

    correctAnswer = calculateDiscount(129.99, 65.5)
    assert calculateDiscount(129.99, 65.5) == pytest.approx(correctAnswer)

# This function will test the discount function with both an integer and a float variable.
def testDiscountMixed():

    correctAnswer = calculateDiscount(175.10, 70)
    assert calculateDiscount(175.10, 70) == pytest.approx(correctAnswer)