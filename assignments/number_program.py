"""
This program takes ten consecutive numbers (0-10) and computes the sum of those numbers.
"""
numbers = list(range(0, 11))
total = sum(numbers)
print("Numbers:", numbers)
print("Sum:", total)


"""
This program takes ten consecutive numbers (0-10) and computes the sum of even and odd numbers separately.
"""
numbers = list(range(0, 11))

even_numbers = [n for n in numbers if n % 2 == 0]
odd_numbers = [n for n in numbers if n % 2 != 0]

even_sum = sum(even_numbers)
odd_sum = sum(odd_numbers)

print("Even numbers:", even_numbers)
print("Sum of even numbers:", even_sum)
print("Odd numbers:", odd_numbers)
print("Sum of odd numbers:", odd_sum)

