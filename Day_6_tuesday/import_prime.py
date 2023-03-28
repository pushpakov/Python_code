# importing function from other module and trying to run the function again on try and except block:


from prime_num import print_primes as prime
import sys

def print_prime(num):
    try:
        return prime(num)
    except:
        return ("Error :" ,sys.exc_info()[0] )

print(print_prime(20)) 




