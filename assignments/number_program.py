# calculates the sum of numbers from 0 to 10
#New changes for merging
# The range(0, 11) generates numbers from 0 up to but not including 11
numbers = range(0, 11)

# Use the sum function to add all numbers in the range
total_sum = sum(numbers)

# Print the result
print("The sum of numbers from 0 to 10 is:", total_sum)

"""
Function to compute even numbers and their sum from a given list of numbers.
"""

def get_even_and_sum(numbers):
    even_numbers = [n for n in numbers if n % 2 == 0]
    even_sum = sum(even_numbers)
    return even_numbers, even_sum


numbers = list(range(0, 11))
even_numbers, even_sum = get_even_and_sum(numbers)
print("Even numbers:", even_numbers)
print("Sum of even numbers:", even_sum)

