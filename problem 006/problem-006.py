# Sum Square Difference
# import statements here
import math

# Function definition for Sum of Squares to a given number as parameter
def sumOfSquaresToN(N):
	summation = 0
	for i in range(1, (N+1)):
		tempvar = math.pow(i,2)
		summation += tempvar
	return summation

# Function definition for Square of Sums to a given number as parameter
def squareOfSumsToM(M):
	fullsum = 0
	for j in range(1, (M+1)):
		fullsum += j
	squaredsum = math.pow(fullsum,2)
	return squaredsum

# Actual solution to the problem, using the previously defined functions
def differenceofsofsqandsqofs(N,M):
	return(squareOfSumsToM(M) - sumOfSquaresToN(N))
