# fibonacci number module 

 # return Fibonacci series up to n


def fib(n):  
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result


print(fib(21))