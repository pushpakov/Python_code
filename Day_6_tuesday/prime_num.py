def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def print_primes(num):
    try:
        num = int(num)
        if num < 2:
            raise ValueError("Number should be greater than 1")
        primes = []
        for i in range(2, num+1):
            if is_prime(i):
                primes.append(i)
        # print(primes)
        return primes
    except ValueError as e:
        print(e)
        return []

# # executing module as script
if __name__ == "__main__":
    print(print_primes(20)) 
