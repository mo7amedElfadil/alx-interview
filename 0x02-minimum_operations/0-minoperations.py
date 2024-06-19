#!/usr/bin/python3
"""
Given a text file with a single character 'H', what is the least number of
operations are requred to result in exactly n H characters in the file.
Allowed operations:
    Copy All
    Paste
"""
from math import sqrt



def minOperations(n: int) -> int:
    """
    minOperations - calculates the fewest number of operations needed to
    result in exactly n H characters in the file.
    Description:
        To solve this problem, we need to find the smallest factor of n
        greater than 1. If n is prime, the smallest factor is n itself.
        We then recursively call minOperations on the result of n divided by
        the smallest factor. We add the smallest factor to the result of the
        recursive call. We continue this process until n is less than or equal
        to 1. The number of operations is the sum of the smallest factors
        found in each recursive call.
    Arguments:
        n - integer: number of H characters to achieve
    Returns:
        number of operations or 0 if n is impossible to achieve
    """
    if n <= 1:
        return 0
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return i + minOperations(n // i)

    return n

primes_cache = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]


def minOperationsCaching(n: int) -> int:
    """
    minOperations - calculates the fewest number of operations needed to
    result in exactly n H characters in the file.
    Description:
        To solve this problem, we need to find the smallest factor of n
        greater than 1. If n is prime, the smallest factor is n itself.
        We then recursively call minOperations on the result of n divided by
        the smallest factor. We add the smallest factor to the result of the
        recursive call. We continue this process until n is less than or equal
        to 1. The number of operations is the sum of the smallest factors
        found in each recursive call.
    Arguments:
        n - integer: number of H characters to achieve
    Returns:
        number of operations or 0 if n is impossible to achieve
    """
    if n <= 1:
        return 0
    for i in primes_cache:
        if n % i == 0:
            return i + minOperations(n // i)
    for i in range(primes_cache[-1], int(sqrt(n)) + 1):
        if n % i == 0:
            primes_cache.append(i)
            return i + minOperations(n // i)

    return n


def minOperationsOptimized(n: int) -> int:
    """
    minOperations - calculates the fewest number of operations needed to
    result in exactly n H characters in the file.
    Description:
        To solve this problem, we need to find the smallest factor of n
        greater than 1. If n is prime, the smallest factor is n itself.
        We then recursively call minOperations on the result of n divided by
        the smallest factor. We add the smallest factor to the result of the
        recursive call. We continue this process until n is less than or equal
        to 1. The number of operations is the sum of the smallest factors
        found in each recursive call.
    Arguments:
        n - integer: number of H characters to achieve
    Returns:
        number of operations or 0 if n is impossible to achieve
    """
    if n <= 1:
        return 0
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            power = 0
            while n % i == 0:
                n //= i
                power += 1
            return power * i + minOperationsOptimized(n)

    return n


from functools import lru_cache

@lru_cache(maxsize=None)
def minOperationsCached(n: int) -> int:
    """
    minOperations - calculates the fewest number of operations needed to result in exactly n H characters in the file.

    Description:
    To solve this problem, we need to find the smallest factor of n greater than 1. If n is prime, the smallest factor is n itself.
    We then recursively call minOperations on the result of n divided by the smallest factor. We add the smallest factor to the result of the recursive call.
    We continue this process until n is less than or equal to 1. The number of operations is the sum of the smallest factors found in each recursive call.

    Arguments:
    n - integer: number of H characters to achieve

    Returns:
    number of operations or 0 if n is impossible to achieve
    """
    if n <= 1:
        return 0

    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            power = 0
            while n % i == 0:
                n //= i
                power += 1
            return power * i + minOperationsCached(n)

    return n




# Initialize the cache with some small prime numbers
prime_cache = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

def extend_primes_cache(limit: int):
    """Extend the prime cache up to the given limit using the Sieve of Eratosthenes."""
    if prime_cache[-1] >= limit:
        return

    is_prime = [True] * (limit + 1)
    for p in prime_cache:
        for multiple in range(p * p, limit + 1, p):
            is_prime[multiple] = False

    for num in range(prime_cache[-1] + 1, limit + 1):
        if is_prime[num]:
            prime_cache.append(num)

@lru_cache(None)
def minOperationsCachingGPT(n: int) -> int:
    """
    minOperationsCaching - calculates the fewest number of operations needed to
    result in exactly n H characters in the file.
    """
    if n <= 1:
        return 0

    limit = int(sqrt(n)) + 1
    extend_primes_cache(limit)

    for prime in prime_cache:
        if prime > limit:
            break
        if n % prime == 0:
            return prime + minOperationsCachingGPT(n // prime)

    return n



expected = {1:0, 2:2, 3:3, 5:5, 7:7, 11:11, 13:13, 17:17, 19:19, 23:23, 29:29}


def minOperationsC(n: int) -> int:
    """
    minOperations - calculates the fewest number of operations needed to
    result in exactly n H characters in the file.
    Description:
        To solve this problem, we need to find the smallest factor of n
        greater than 1. If n is prime, the smallest factor is n itself.
        We then recursively call minOperations on the result of n divided by
        the smallest factor. We add the smallest factor to the result of the
        recursive call. We continue this process until n is less than or equal
        to 1. The number of operations is the sum of the smallest factors
        found in each recursive call.
    Arguments:
        n - integer: number of H characters to achieve
    Returns:
        number of operations or 0 if n is impossible to achieve
    """
    if n <= 1:
        return 0
    if n in expected:
        return expected[n]
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            expected[n] = i + minOperationsC(n // i)
            return expected[n]
    return n

