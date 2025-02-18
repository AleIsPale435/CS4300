
# This function will determine if a number is positive, negative, or zero.
def checkNumber(number):

    # String variable to determine what kind of number it is.
    numberStatus = "null"

    # If statements that changes the string based on which condition is met.
    if (number > 0):
        numberStatus = "Positive"
    elif (number < 0):
        numberStatus = "Negative"
    else:
        numberStatus = "Zero"
    
    return numberStatus

# This function will find the first 10 prime numbers
def firstTenPrimeNumbers():

    # Primes is a list variable that will be added with each prime number. The primeNum variable has to start with 2 since it is the first prime number.
    primes = []
    primeNum = 2

    # This while loop will iterate through until the primes list hits 10 numbers.
    while len(primes) < 10:

        # Boolean flag to represent if a number is prime
        numIsPrime = True

        # This for loop will check if a number is prime by checking divisibility from 2 to its square root.
        for i in range(2, int(primeNum**0.5) + 1):
            if primeNum % i == 0:
                numIsPrime = False
                break
        
        # If a number is prime, it will be added to the primes list.
        if numIsPrime:
            primes.append(primeNum)
        
        # Number iterates by 1 each while loop iteration
        primeNum += 1
    return primes

# This function will return the sum of the first 100 numbers.
def sumOfNumbers():
    
    # Total variable will hold the sum and the number variable starts at 1.
    total = 0
    number = 1

    # This while loop will continue to iterate until the number variable hits 100.
    while (number <= 100):

        # The total sum will be added to whatever the number variable is at and the number variable will iterate 1 each time
        total += number
        number += 1
    return total
        
if __name__ == "__main__":
    
    # Asks user to input number to check for positive, negative or zero.
    number = int(input("Enter a number: "))
    print("The number is {checkNumber(number)}")

    # For loop to print the first 10 numbers.
    print("First ten prime numbers:")
    primes = firstTenPrimeNumbers()
    for prime in primes:
        print(prime, end=" ")
    print()
    
    # Print the sum of numbers 1-100
    print("The sum of the numbers 1-100 is: ", sumOfNumbers())