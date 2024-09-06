# Prime Number Checker
# Your task is to develop a function is_prime_number in Python that checks if a given number is a prime number. The function should return True if the number is prime, and False otherwise.

# Function Requirements
# Name: is_prime_number
# Input: A single number (can be positive, negative, or a floating point number).
# Output: True if the number is a prime number, False otherwise.
# Examples
# is_prime_number(5) should return True, as 5 is a prime number.
# is_prime_number(4) should return False, as 4 is not a prime number.
# Key Points
# Ensure your function handles a variety of cases, including negative numbers and non-integer values, as they will be part of the challenges.
# Your implementation should efficiently determine the primality of a number.
# Good luck, and happy coding!

def is_prime_number(n):
    # Check if n is an integer
    if not isinstance(n, int) or n <= 1:
        return False
    
    # Prime numbers must be greater than 1
    if n == 2:
        return True  # 2 is the only even prime number
    if n % 2 == 0:
        return False  # No other even number can be prime

    # Check for divisibility by odd numbers up to √n
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

# Test cases
print(is_prime_number(5))  # True
print(is_prime_number(4))  # False
print(is_prime_number(-5)) # False
print(is_prime_number(2.5)) # False
print(is_prime_number(2))  # True
