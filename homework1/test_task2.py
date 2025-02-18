import task2

# Test case for integer function, checks if its an integer and if it is the correct answer.
def testGetInteger():
    assert isinstance(task2.getInteger(), int)
    assert task2.getInteger() == 5
# Test case for float function, checks if it is a float and if it is the correct answer.
def testGetFloat():
    assert isinstance(task2.getFloat(), float)
    assert task2.getFloat() == 27.2034

# Test case for string function, checks if it is a string and if the concatenation of strings matches the answer.
def testGetString():
    assert isinstance(task2.getString(), str)
    assert task2.getString() == "Task 2 Status: Complete"

# Test case for boolean function, checks if it is a boolean and if the function returned true.
def testGetBoolean():
    assert isinstance(task2.getBoolean(), bool)
    assert task2.getBoolean() is True
