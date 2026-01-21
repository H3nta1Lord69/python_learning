
# is vs ==
a = [1, 2, 3]
b = a
c = [1, 2, 3]
print(a == b)  # True, because values are the same
print(a is b)  # True, because both refer to the same object
print(a == c)  # True, because values are the same
print(a is c)  # False, because they are different objects in memory
print(id(a))    # Memory address of a
print(id(b))    # Memory address of b (same as a)
print(id(c))    # Memory address of c (different from a and b)
print(a is not c)  # True, because they are different objects
print(a != c)     # False, because values are the same
print(a is not b)  # False, because both refer to the same object
print(a != b)     # False, because values are the same
print((a is b) == (a == b))  # True, both are True
print((a is c) == (a == c))  # False, is is False but == is True
print((a is not c) != (a != c))  # False, both are True
print((a is not b) != (a != b))  # True, both are False
print(type(a is b))  # <class 'bool'>
print(type(a == b))  # <class 'bool'>
print(type(a is c))  # <class 'bool'>
print(type(a == c))  # <class 'bool'>
print((a is b) and (a == b))  # True, both are True
print((a is c) or (a == c))   # True, one is True
print(not (a is c))  # True, because a is not c
print(not (a == c))  # False, because a equals c
print((a is b) if True else (a is c))  # True, because a is b
print((a == b) if False else (a == c))  # True, because a equals c
print((a is c) if True else (a is b))  # False, because a is not c
print((a == c) if False else (a == b))  # True, because a equals b
print((a is b) == True)  # True, because a is b
print((a == b) == True)  # True, because a equals b
print((a is c) == False)  # True, because a is not c
print((a == c) == True)  # True, because a equals c
print((a is not c) == True)  # True, because a is not c
print((a != c) == False)  # True, because a equals c
print((a is not b) == False)  # True, because a is b
print((a != b) == False)  # True, because a equals b
print((a is b) and not (a is c))  # True, a is b and a is not c
print((a == b) or not (a == c))   # True, a equals b
print((a is c) or (a is b))  # True, a is b
print((a == c) and (a == b))  # True, a equals b
print((a is not c) and (a is b))  # True, a is b and a is not c
print((a != c) or (a == b))   # True, a equals b
print((a is not b) or (a is c))  # False, both are False
print((a != b) and (a == c))   # True, a equals c
print((a is b) if (a == c) else (a is c))  # True, because a is b
print((a == b) if (a is c) else (a == c))  # True, because a equals c
print((a is c) if (a is b) else (a is not c))  # False, because a is not c
print((a == c) if (a == b) else (a != c))  # True, because a equals c
print((a is b) == (a is not c))  # True, both are True
print((a == b) == (a != c))  # False, is True but != is False
print((a is c) == (a is not b))  # True, both are False
print((a == c) == (a == b))  # True, both are True
print(bool(a is b))  # True, because a is b
print(bool(a == b))  # True, because a equals b
print(bool(a is c))  # False, because a is not c
print(bool(a == c))  # True, because a equals c
print((a is b) is True)  # True, because a is b
print((a == b) is True)  # True, because a equals b
print((a is c) is False)  # True, because a is not c
print((a == c) is True)  # True, because a equals c
print((a is not c) is True)  # True, because a is not c
print((a != c) is False)  # True, because a equals c 
print((a is not b) is False)  # True, because a is b
print((a != b) is False)  # True, because a equals b
print((a is b) and (a is not c))  # True, a is b and a is not c
print((a == b) or (a != c))   # True, a equals b
print((a is c) or (a is b))  # True, a is b
print((a == c) and (a == b))  # True, a equals b
print((a is not c) and (a is b))  # True, a is b and a is not c
print((a != c) or (a == b))   # True, a equals b
print((a is not b) or (a is c))  # False, both are False
print((a != b) and (a == c))   # True, a equals c
print((a is b) if (a == c) else (a is c))  # True, because a is b
print((a == b) if (a is c) else (a == c))  # True, because a equals c
print((a is c) if (a is b) else (a is not c))  # False, because a is not c
print((a == c) if (a == b) else (a != c))  # True, because a equals c
print((a is b) == (a is not c))  # True, both are True