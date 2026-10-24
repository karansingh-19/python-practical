# Practical 2 :

import math

def is_prime(num):
    """Return True if num is prime, else False."""
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def primes_till_n(n):
    """Return a list of all primes from 2 to n."""
    result = []
    for i in range(2, n + 1):
        if is_prime(i):
            result.append(i)
    return result

def first_n_primes(n):
    """Return a list of the first n prime numbers."""
    result = []
    num = 2
    while len(result) < n:
        if is_prime(num):
            result.append(num)
        num += 1
    return result

# Main program
n = int(input("Enter a number n: "))

# a. Check if n is prime
if is_prime(n):
    print(n, "is a prime number.")
else:
    print(n, "is not a prime number.")

# b. All primes till n
print("Prime numbers till", n, ":", primes_till_n(n))

# c. First n primes
print("First", n, "prime numbers:", first_n_primes(n))