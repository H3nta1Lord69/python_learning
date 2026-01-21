
# Membership Operators
# Membership operators are used to test whether a value or variable is found in a sequence (such as a string, list, tuple, or dictionary).
# The two membership operators are 'in' and 'not in'.

# 'in' Operator
# The 'in' operator returns True if the specified value is found in the sequence, otherwise it returns False.
fruits = ["apple", "banana", "cherry"]
print("banana" in fruits)  # Output: True
print("grape" in fruits)   # Output: False

# 'not in' Operator
# The 'not in' operator returns True if the specified value is not found in the sequence, otherwise it returns False.
print("banana" not in fruits)  # Output: False
print("grape" not in fruits)   # Output: True

# Example with Strings
text = "Hello, welcome to the world of Python."
print("Python" in text)      # Output: True
print("Java" not in text)    # Output: True
# Membership operators are case-sensitive when used with strings.
print("hello" in text)      # Output: False
print("Hello" in text)      # Output: True

# Example with Dictionaries
my_dict = {"name": "Alice", "age": 25}
print("name" in my_dict)      # Output: True
print("address" not in my_dict)  # Output: True
# Note: When using membership operators with dictionaries, they check for the presence of keys, not values.

# Example with Tuples
my_tuple = (1, 2, 3, 4, 5)
print(3 in my_tuple)        # Output: True
print(6 not in my_tuple)    # Output: True
# You can use membership operators in conditional statements to execute code based on the presence or absence of a value in a sequence.
if "cherry" in fruits:
    print("Cherry is in the fruit list!")  # Output: Cherry is in the fruit list!
if "grape" not in fruits:
    print("Grape is not in the fruit list!")  # Output: Grape is not in the fruit list!
    
# Membership operators are a powerful way to check for the existence of elements in various data structures in Python.
# They are commonly used in conditional statements and loops to control the flow of a program based on the presence or absence of specific values.

# Summary
# - 'in' operator checks if a value exists in a sequence and returns True or False
# - 'not in' operator checks if a value does not exist in a sequence and returns True or False