
# Data conversion examples in Python
# Converting between different data types
# Integer to Float
int_value = 10
float_value = float(int_value)
print(f"Integer {int_value} converted to Float: {float_value}")

# Float to Integer
float_value = 3.14
int_value = int(float_value)
print(f"Float {float_value} converted to Integer: {int_value}")

# String to Integer
str_num = "123"
int_num = int(str_num)
print(f"String '{str_num}' converted to Integer: {int_num}")

# String to Float
str_float = "45.67"
float_num = float(str_float)
print(f"String '{str_float}' converted to Float: {float_num}")

# Integer to String
int_val = 42
str_val = str(int_val)
print(f"Integer {int_val} converted to String: '{str_val}'")

# Float to String
float_val = 3.14159
str_val = str(float_val)
print(f"Float {float_val} converted to String: '{str_val}'")

# String to List
str_list = "hello"
list_val = list(str_list)
print(f"String '{str_list}' converted to List: {list_val}")

# List to String
list_chars = ['h', 'e', 'l', 'l', 'o']
str_from_list = ''.join(list_chars)
print(f"List {list_chars} converted to String: '{str_from_list}'")

# Tuple to List
tuple_val = (1, 2, 3)
list_from_tuple = list(tuple_val)
print(f"Tuple {tuple_val} converted to List: {list_from_tuple}")

# List to Tuple
list_val = [4, 5, 6]
tuple_from_list = tuple(list_val)
print(f"List {list_val} converted to Tuple: {tuple_from_list}")

# Dictionary to List of Keys
dict_val = {'a': 1, 'b': 2, 'c': 3 }
list_of_keys = list(dict_val.keys())
print(f"Dictionary {dict_val} converted to List of Keys: {list_of_keys}")

# Dictionary to List of Values
list_of_values = list(dict_val.values())
print(f"Dictionary {dict_val} converted to List of Values: {list_of_values}")

# List of Tuples to Dictionary
list_of_tuples = [('x', 10), ('y', 20), ('z', 30)]
dict_from_tuples = dict(list_of_tuples)
print(f"List of Tuples {list_of_tuples} converted to Dictionary: {dict_from_tuples}")

# Set to List
set_val = {1, 2, 3, 4}
list_from_set = list(set_val)
print(f"Set {set_val} converted to List: {list_from_set}")

# List to Set
list_with_duplicates = [1, 2, 2, 3, 4, 4]
set_from_list = set(list_with_duplicates)
print(f"List {list_with_duplicates} converted to Set: {set_from_list}")

# Boolean to Integer
bool_val = True
int_from_bool = int(bool_val)
print(f"Boolean {bool_val} converted to Integer: {int_from_bool}")

# Integer to Boolean
int_val = 0
bool_from_int = bool(int_val)
print(f"Integer {int_val} converted to Boolean: {bool_from_int}")