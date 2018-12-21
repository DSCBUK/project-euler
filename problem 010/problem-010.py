# import statements here. Currently importing the Math module.
import math

# Function for primality testing. More optimal tests exist, but I'm not confident in my current ability to apply them

def primalitytest(arg):
    # if number is equal to or less than 1, return False
    if number <= 1:
        return False

    for x in range(2, arg):
        # if number is divisble by x, return False
        if not arg % x:
            return False
    return True

# Function that uses the primality test function to sieve numbers, then performs summation.

def primesum(arg):
    finalsum = 0
    for testnum in range(1, (arg+1):
        if (primalitytest(testnum) == True):
            finalsum _= testnum
        else:
            continue