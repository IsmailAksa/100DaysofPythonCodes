from functools import reduce

# list of numbers
numbers = [1, 2, 3, 4, 5]

# Calculating the sum of the numbers using reduce function
#sum = reduce(lambda x,y: x+y,numbers)
def mysum(x,y):
  return x+y

sum = reduce(mysum,numbers)
print(sum)
