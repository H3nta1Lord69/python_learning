
# Incorporated Functions
# ==========================
# In Python, functions can be defined within other functions. These are known as
# incorporated functions or nested functions. They can be useful for encapsulating
# functionality that is only relevant within the outer function. Here’s an example:
def outer_function(x):
    def inner_function(y):
        return y * 2
    result = inner_function(x)
    return result + 3
print(outer_function(5))  # Output: 13
# In this example, `inner_function` is defined within `outer_function`. It takes a
# parameter `y` and returns its double. The `outer_function` calls `inner_function
# with the argument `x`, adds 3 to the result, and returns it.
# Incorporated functions can also access variables from the enclosing scope:
def outer_function_with_variable(x):
    offset = 10
    def inner_function(y):
        return y + offset
    return inner_function(x)
print(outer_function_with_variable(5))  # Output: 15
# Here, `inner_function` accesses the `offset` variable defined in `outer_function`.
# This allows for more modular and organized code, especially when the inner function
# is not needed outside the context of the outer function.
# Incorporated functions can also be used for creating closures, where the inner
# function retains access to the outer function's scope even after the outer function
# has finished executing. This can be useful for maintaining state or creating
# function factories.
def make_multiplier(factor):
    def multiply(x):
        return x * factor
    return multiply
double = make_multiplier(2)
triple = make_multiplier(3)
print(double(5))  # Output: 10
print(triple(5))  # Output: 15
# In this example, `make_multiplier` returns the `multiply` function, which retains
# access to the `factor` variable from its enclosing scope. This allows us to create
# specialized multiplier functions like `double` and `triple`.
# Incorporated functions are a powerful feature in Python that can help improve code
# organization and encapsulation. They are particularly useful for creating helper
# functions that are only relevant within the context of a specific outer function.
# Remember to use them judiciously, as excessive nesting can sometimes make code
# harder to read and maintain.

# Functions methods
# ==========================
# In Python, functions are first-class objects, which means they can have methods
# associated with them. One of the most commonly used methods for functions is the
# `__name__` attribute, which returns the name of the function as a string. Here’s an example:
def sample_function():
    pass
print(sample_function.__name__)  # Output: sample_function
# In addition to `__name__`, functions also have other attributes and methods, such as
# `__doc__`, which returns the docstring of the function, and `__code__`, which
# provides access to the compiled bytecode of the function. Here’s an example:
def documented_function():
    """This is a sample function with a docstring."""
    pass
print(documented_function.__doc__)  # Output: This is a sample function with a docstring.
# Functions also have a `__call__` method, which allows you to call the function
# programmatically. Here’s an example:
def callable_function(x):
    return x * 2
result = callable_function.__call__(5)
print(result)  # Output: 10
# In this example, we use the `__call__` method to invoke `callable_function` with
# the argument `5`, which returns `10`.
# Another useful method is `__defaults__`, which returns a tuple containing the
# default values for the function's parameters. Here’s an example:  
def function_with_defaults(a, b=2, c=3):
    return a + b + c
print(function_with_defaults.__defaults__)  # Output: (2, 3)
# This shows that the default values for parameters `b` and `c` are `2
# and `3`, respectively.
# Functions in Python have several other attributes and methods that can be useful
# for introspection and manipulation. Some of these include `__annotations__`,
# `__kwdefaults__`, and `__globals__`. Understanding these methods can help you
# work more effectively with functions in Python.
# Overall, function methods provide valuable insights into the properties and
# behavior of functions in Python, allowing for greater flexibility and control
# when working with them.

# Note: While accessing function methods directly is possible, it's generally
# recommended to use built-in functions like `getattr()` for better readability
# and maintainability of your code.