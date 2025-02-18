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

if __name__ == "__main__":

    # Calls all of the functions.
    print(getInteger())
    print(getFloat())
    print(getString())
    print(getBoolean())