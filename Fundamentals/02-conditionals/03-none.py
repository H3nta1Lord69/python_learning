
# None
a = None
if a is None:
    print("a is None")
else:
    print("a is not None")

# Checking for None using 'is' operator
b = 5
if b is not None:
    print("b is not None")
else:
    print("b is None")
    
# Using None in a function
def check_value(value):
    if value is None:
        return "Value is None"
    else:
        return "Value is not None"
print(check_value(None)) # Value is None
print(check_value(10)) # Value is not None

# None as a default parameter
def greet(name=None):
    if name is None:
        return "Hello, Guest!"
    else:
        return f"Hello, {name}!"
      
print(greet()) # Hello, Guest!
print(greet("Alice")) # Hello, Alice!