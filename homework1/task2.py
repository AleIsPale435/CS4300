# This tasks will return the sum of two integers.
def getInteger():
    a = 2
    b = 3
    return a + b

# This function will return the product of two float values.
def getFloat():
    c = 7.62
    d = 3.57
    return c * d

# This function will return the concatenation of two strings.
def getString():
    str1 = "Task 2 Status: " 
    str2 = "Complete"
    return str1 + str2

# This function will return the result of the boolean expression.
def getBoolean():
    trueFlag = True 
    falseFlag = False 
    return trueFlag and not falseFlag

# Test case for integer function, checks if its an integer and if it is the correct answer.
def testGetInteger():
    assert isinstance(getInteger(), int)
    assert getInteger() == 5
# Test case for float function, checks if it is a float and if it is the correct answer.
def testGetFloat():
    assert isinstance(getFloat(), float)
    assert getFloat() == 27.2034

# Test case for string function, checks if it is a string and if the concatenation of strings matches the answer.
def testGetString():
    assert isinstance(getString(), str)
    assert getString() == "Task 2 Status: Complete"

# Test case for boolean function, checks if it is a boolean and if the function returned true.
def testGetBoolean():
    assert isinstance(getBoolean(), bool)
    assert getBoolean() is True
