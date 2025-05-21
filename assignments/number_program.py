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

