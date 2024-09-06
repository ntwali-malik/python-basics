# Square Numbers
# In this lab, you will develop a Python function named square_numbers. This function should take a list of numbers as input and return a new list containing the squares of each number.

# Function Requirements:
# Squaring Numbers: The function should square each number in the input list.

# Example:
# Input: [2, 3]
# Output: [4, 9]
# Handling Different Types of Numbers:

# For positive and negative integers, return their squares.
# For floating point numbers, return their squares rounded to two decimal places.
# Example:
# Input: [-2, 2.3]
# Output: [4, 5.29]
# Empty Array Handling: If an empty array is passed, the function should return an empty array.

# Example:
# Input: []
# Output: []
# Constraints:
# The function must handle both integers and floating point numbers.
# For floating point numbers, the squared result should be rounded to two decimal places.
# An empty input list should result in an empty output list.

def square_numbers(numbers):
    # Return a new list with squared values
    return [round(num ** 2, 2) if isinstance(num, float) else num ** 2 for num in numbers]

# Test cases
print(square_numbers([2, 3]))  # [4, 9]
print(square_numbers([-2, 2.3]))  # [4, 5.29]
print(square_numbers([]))  # []
print(square_numbers([1.5, -3, 0]))  # [2.25, 9, 0]
