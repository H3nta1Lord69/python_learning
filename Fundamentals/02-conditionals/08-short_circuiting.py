
# Short circuiting in Python refers to the behavior of logical operators
# (and, or) where the second operand is evaluated only if necessary.
# This can be useful for optimizing code and avoiding unnecessary computations.
# Example of short-circuiting with 'and'
def is_even_and_positive(num):
    return num > 0 and num % 2 == 0 # True if num is positive and even
# Example of short-circuiting with 'or'
def is_even_or_positive(num):
    return num % 2 == 0 or num > 0 # True if num is even or positive
# Testing the functions
print(is_even_and_positive(4))  # True
print(is_even_and_positive(-2)) # False
print(is_even_or_positive(3))   # True
print(is_even_or_positive(-4))  # True
print(is_even_or_positive(-3))  # False
# Demonstrating short-circuiting behavior
def divide_if_non_zero(num, denom):
    return denom != 0 and (num / denom) # Only divides if denom is not zero
print(divide_if_non_zero(10, 2))  # 5.0
print(divide_if_non_zero(10, 0))  # False (no division by zero error)
def safe_divide(num, denom):
    return denom == 0 or (num / denom) # Returns True if denom is zero, else performs division
print(safe_divide(10, 2))  # 5.0
print(safe_divide(10, 0))  # True (indicates division by zero)