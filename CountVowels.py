# Count Vowels
# In this lab, you will write a Python function named count_vowels. This function takes a single string as input and returns a dictionary. The dictionary should contain counts of each vowel ('a', 'e', 'i', 'o', 'u') found in the string. It's important to note that the function should be case-insensitive and include all vowels in the dictionary, even if their count is zero.

# Function Output
# The output should be a dictionary.
# Each key is a vowel ('a', 'e', 'i', 'o', 'u').
# The value for each key is the count of that vowel in the input string.
# Include all vowels in the dictionary, even with a count of 0 if they are absent.
# Examples
# Example 1:

# Input: "Hello World"
# Output: {'a': 0, 'e': 1, 'i': 0, 'o': 2, 'u': 0}
# Example 2:

# Input: "Python Programming is Awesome"
# Output: {'a': 2, 'e': 2, 'i': 2, 'o': 3, 'u': 0}
# Implement the count_vowels function following these specifications. Good luck!

def count_vowels(s):
    # Initialize the dictionary with vowels set to 0
    vowels = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
    
    # Convert the string to lowercase to make it case-insensitive
    s = s.lower()
    
    # Count each vowel in the string
    for char in s:
        if char in vowels:
            vowels[char] += 1
    
    return vowels

# Test cases
print(count_vowels("Hello World"))  # {'a': 0, 'e': 1, 'i': 0, 'o': 2, 'u': 0}
print(count_vowels("Python Programming is Awesome"))  # {'a': 2, 'e': 2, 'i': 2, 'o': 3, 'u': 0}
