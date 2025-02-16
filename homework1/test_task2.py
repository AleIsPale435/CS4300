import task2

def testGetInteger():
    assert isinstance(task2.getInteger(), int)
    assert task2.getInteger() == 4

def testGetFloat():
    assert isinstance(task2.getFloat(), float)
    assert task2.getFloat() == 1.42

def testGetString():
    assert isinstance(task2.getString(), str)
    assert task2.getString() == "This is a string."

def testGetBoolean():
    assert isinstance(task2.getBoolean(), bool)
    assert task2.getBoolean() is True
