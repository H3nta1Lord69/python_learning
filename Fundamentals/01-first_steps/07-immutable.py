
# Variables in Python can be reassigned, but some data types are immutable,
# meaning their value cannot be changed after they are created.
# Immutable data types include:
# 1. Integers
num = 10
print(type(num))  # <class 'int'>
# num[0] = 5  # This will raise an error because integers are immutable.
# 2. Floats
pi = 3.14
print(type(pi))  # <class 'float'>
# pi[0] = 3.15  # This will raise an error because floats are immutable.
# 3. Strings
greeting = "Hello"
print(type(greeting))  # <class 'str'>
# greeting[0] = 'h'  # This will raise an error because strings are immutable.
# 4. Tuples
coordinates = (10, 20)
print(type(coordinates))  # <class 'tuple'>
# coordinates[0] = 15  # This will raise an error because tuples are immutable
# 5. Frozensets
fset = frozenset([1, 2, 3])
print(type(fset))  # <class 'frozenset'>
# fset.add(4)  # This will raise an error because frozensets are immutable.
# To "change" an immutable object, you must create a new object.
# For example, to change a string:
new_greeting = greeting.replace("H", "h")
print(new_greeting)  # "hello"
# To change a tuple:
new_coordinates = (15, coordinates[1])
print(new_coordinates)  # (15, 20)
# Understanding immutability is important for writing efficient and bug-free code in Python.
# It helps you know when you need to create new objects versus modifying existing ones.
# Remember that while the objects themselves are immutable, you can always reassign variables to new objects.
# Example of reassigning a variable
num = 20  # Now num points to a new integer object
print(num)  # 20
num += 5  # This creates a new integer object and reassigns num
print(num)  # 25