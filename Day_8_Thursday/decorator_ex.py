"""
 decorator is a special type of function that takes another function as input and returns a new function as output. The new function can modify the behavior of the input function or add new functionality to it, without modifying its source code. Decorators are commonly used in Python to add functionality such as logging, authentication, and caching to functions or methods. Here is an example of a simple decorator that adds logging to a function
"""


def log_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Calling function {func.__name__} with args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        print(f"Function {func.__name__} returned {result}")
        return result
    return wrapper

@log_decorator
def add_numbers(a, b):
    return a + b

result = add_numbers(2, 3)   # Output: "Calling function add_numbers with args=(2, 3), kwargs={}"
                             #         "Function add_numbers returned 5"
print(result) 