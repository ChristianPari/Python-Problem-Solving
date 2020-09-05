# Write a function that takes a non-negative integer and return its factorial.

def factorial(num):
    total = 1
    for i in range(1, num + 1):
        total *= i
    return(total)


factorial(3)
