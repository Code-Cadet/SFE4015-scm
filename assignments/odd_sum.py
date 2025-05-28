def get_odd_numbers(start, end):
    """
    Returns a list of odd numbers between start and end (inclusive).
    """
    return [num for num in range(start, end + 1) if num % 2 != 0]


def sum_odd_numbers(start, end):
    """
    Returns the sum of odd numbers between start and end (inclusive).
    """
    odd_numbers = get_odd_numbers(start, end)
    return sum(odd_numbers)


# Example usage:
start = 1
end = 10

odd_list = get_odd_numbers(start, end)
odd_sum = sum_odd_numbers(start, end)

print(f"Odd numbers from {start} to {end}: {odd_list}")
print(f"Sum of odd numbers from {start} to {end}: {odd_sum}")
