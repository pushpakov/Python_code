"""
generator is a special type of function that returns an iterable sequence of values one at a time, rather than returning a complete list or tuple all at once. Generators are useful for generating large amounts of data on-the-fly without consuming excessive amounts of memory, as well as for implementing custom iteration patterns. In Python, generators are implemented using the yield keyword. Here is an example of a simple generator that generates a sequence of Fibonacci numbers
"""

def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

fib = fibonacci()
for i in range(10):
    print(next(fib))   # Output: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34

