
# Truthy and Falsey Values in Python
# In Python, certain values are considered "truthy" or "falsey" when evaluated in a boolean context.
# Falsey values include:
# - None
# - False
# - 0 (zero of any numeric type)
# - Empty sequences and collections (e.g., '', [], {}, set())
# All other values are considered truthy.
def check_truthy_falsey(value):
    if value:
        return "Truthy"
    else:
        return "Falsey"
      
# Test cases
print(check_truthy_falsey(None))        # Output: Falsey
print(check_truthy_falsey(False))       # Output: Falsey
print(check_truthy_falsey(0))           # Output: Falsey
print(check_truthy_falsey(''))          # Output: Falsey
print(check_truthy_falsey([]))          # Output: Falsey
print(check_truthy_falsey({}))          # Output: Falsey
print(check_truthy_falsey(set()))       # Output: Falsey
print(check_truthy_falsey(42))          # Output: Truthy
print(check_truthy_falsey('Hello'))     # Output: Truthy
print(check_truthy_falsey([1, 2, 3]))   # Output: Truthy
print(check_truthy_falsey({'key': 'value'}))  # Output: Truthy
print(check_truthy_falsey({1, 2, 3}))   # Output: Truthy
print(check_truthy_falsey(3.14))        # Output: Truthy
print(check_truthy_falsey(True))        # Output: Truthy