
# Logical Operators
# Logical operators are used to combine conditional statements.
# The most common logical operators are "and", "or", and "not".
# Example of "and" operator
a = 10
b = 5
if a > 0 and b > 0:
    print("Both a and b are positive numbers.")

# Example of "or" operator
if a > 0 or b < 0:
    print("At least one of a or b is a positive number.")

# Example of "not" operator
if not a < 0:
    print("a is not a negative number.")

# Combining multiple logical operators
if (a > 0 and b > 0) or (a < 0 and b < 0):
    print("a and b are either both positive or both negative.")

# Example with nested conditions
if a > 0:
    if b > 0:
        print("Both a and b are positive numbers (nested condition).")
    else:
        print("a is positive, but b is not.")

# Using logical operators in functions
def check_numbers(x, y):
    if x > 0 and y > 0:
        return "Both numbers are positive."
    elif x < 0 or y < 0:
        return "At least one number is negative."
    else:
        return "Both numbers are zero."
result = check_numbers(3, -1)
print(result) # Output: At least one number is negative.
result = check_numbers(2, 4)
print(result) # Output: Both numbers are positive.
result = check_numbers(0, 0)
print(result) # Output: Both numbers are zero.