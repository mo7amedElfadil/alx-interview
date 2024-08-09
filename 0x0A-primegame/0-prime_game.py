#!/usr/bin/python3
""" Prime Game
    Maria and Ben are playing a game. Given a set of consecutive integers
    starting from 1 up to and including n, they take turns choosing a prime
    number from the set and removing that number and its multiples from the
    set. The player that cannot make a move loses the game.

    They play x rounds of the game, where n may be different for each round.
    Assuming Maria always goes first and both players play optimally, determine
    who the winner of each game is.

    Prototype: def isWinner(x, nums)
    where x is the number of rounds and nums is an array of n
    Return: name of the player that won the most rounds
    If the winner cannot be determined, return None
    You can assume n and x will not be larger than 10000
    You cannot import any packages in this task
    Example:

    x = 3, nums = [4, 5, 1]
    First round: 4

    Maria picks 2 and removes 2, 4, leaving 1, 3
    Ben picks 3 and removes 3, leaving 1
    Ben wins because there are no prime numbers left for Maria to choose
    Second round: 5

    Maria picks 2 and removes 2, 4, leaving 1, 3, 5
    Ben picks 3 and removes 3, leaving 1, 5
    Maria picks 5 and removes 5, leaving 1
    Maria wins because there are no prime numbers left for Ben to choose
    Third round: 1

    Ben wins because there are no prime numbers for Maria to choose
    Result: Ben has the most wins
"""


def isPrime(n):
    """ Returns True if n is prime, False otherwise """
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def primeList(n):
    """ Returns a set of prime numbers between a and b
    """
    # primes = [x for x in range(2, b + 1) if isPrime(x)]

    def sieve_of_eratosthenes(n):
        """ Returns a list of prime numbers up to n
        """
        prime = [True] * (n + 1)
        p = 2
        while (p * p <= n):
            if prime[p]:
                for i in range(p * p, n + 1, p):
                    prime[i] = False
            p += 1
        return [p for p in range(2, n + 1) if prime[p]]

    primes = sieve_of_eratosthenes(n)
    return primes


def isWinner(x, nums):
    """ Determines the winner of the prime game
        x: number of rounds
        nums: array of n
        Returns: name of the player that won the most rounds
    """
    players = {"Maria": 0, "Ben": 0}

    for i in range(x):
        primes = primeList(nums[i])
        rounds = len(primes)

        if rounds % 2 == 0:
            players["Ben"] += 1
        else:
            players["Maria"] += 1

    if players["Maria"] > players["Ben"]:
        return "Maria"
    if players["Ben"] > players["Maria"]:
        return "Ben"
    return None
