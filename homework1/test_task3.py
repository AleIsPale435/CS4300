import task3

# Tests the checkNumber function to ensure the positive output works.
def testNumberPositive():
    assert task3.checkNumber(6) == "Positive"

# Tests the checkNumber function to ensure the negative output works.
def testNumberNegative():
    assert task3.checkNumber(-4) == "Negative"

# Tests the checkNumber function to ensure the zero output works.
def testNumberZero():
    assert task3.checkNumber(0) == "Zero"

# Tests the firstTenPrimes function to ensure the first ten prime numbers outputted are correct.
def testFirstTenPrimes():
    
    firstTenPrimeNums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    result = task3.firstTenPrimeNumbers()
    assert result == firstTenPrimeNums

# Tests the sumOfNumbers function to ensure that the sum of the first 100 numbers is correct.
def testSum1To100():

    correctSum = 5050
    result = task3.sumOfNumbers()
    assert result == correctSum