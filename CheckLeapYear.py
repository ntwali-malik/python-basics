# Check Leap Year
# In this lab, you are tasked with writing a Python function named is_leap_year. This function should determine whether a given year is a leap year. A leap year is defined by the following rules:

# A year is a leap year if it is divisible by 4.
# However, if the year is also divisible by 100, it is not a leap year unless it is divisible by 400.
# Your function should take a single input (the year) and return a boolean value: True if the year is a leap year, and False otherwise.

# Examples:
# Input: is_leap_year(2000)
# Expected Output: True
# Explanation: 2000 is divisible by 400, so it is a leap year.

# Input: is_leap_year(1997)
# Expected Output: False
# Explanation: 1997 is not divisible by 4, so it is not a leap year.

# Remember to write clean, readable code and test your function thoroughly to ensure it meets the criteria.
def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True  # Divisible by 400, it's a leap year
            else:
                return False  # Divisible by 100 but not 400, not a leap year
        else:
            return True  # Divisible by 4 but not 100, it's a leap year
    else:
        return False  # Not divisible by 4, not a leap year

# Test cases
print(is_leap_year(2000))  # True
print(is_leap_year(1997))  # False
print(is_leap_year(1900))  # False
print(is_leap_year(2024))  # True
