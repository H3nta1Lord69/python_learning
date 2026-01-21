
# Comparison Operators
# Comparison operators are used to compare two values. They return a boolean value (True or False) based on the comparison.
# Here are some common comparison operators in Python:
# Equal to: ==
# Not equal to: !=
# Greater than: >
# Less than: <
# Greater than or equal to: >=
# Less than or equal to: <=

a = 10
b = 20
print(a == b)  # False, because 10 is not equal to 20
print(a != b)  # True, because 10 is not equal to 20
print(a > b)   # False, because 10 is not greater than 20
print(a < b)   # True, because 10 is less than 20
print(a >= 10) # True, because 10 is greater than or equal to 10
print(b <= 20) # True, because 20 is less than or equal to 20
# You can use comparison operators in conditional statements as well:
if a < b:
    print("a is less than b")
else:
    print("a is not less than b")
# Output: a is less than b
# Comparison operators are essential for making decisions in your code based on the values of variables.