# Problem 1: Sum of Multiples of 3 and 5	betweem 1 and 1000

# Function Definition
def getSum():
  sum = 0
  for x in range(1, 1000):
    if x % 3 == 0 or x % 5 == 0:
      sum += x
  return sum

# Call the function
print(getSum())
