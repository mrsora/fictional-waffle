# Project Euler 3
# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143?


def largestPrimeNumber(n):
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
    return n


print(largestPrimeNumber(13195))
# 29

print(largestPrimeNumber(600851475143))
# 6857
