#!/usr/bin/python3
"""Prime game module"""

def isWinner(x, nums):
    """
    Determines the winner of the prime game.

    Args:
        x (int): Number of rounds.
        nums (list): List of integers representing the number of marbles in each round.

    Returns:
        str: The name of the player who wins the most rounds, or None if there is no winner.
    """
    if not isinstance(x, int) or x <= 0 or not isinstance(nums, list) or not all(isinstance(n, int) and n > 0 for n in nums):
        return None

    def is_prime(n):
        """Check if a number is prime."""
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    primes = [i for i in range(2, max(nums) + 1) if is_prime(i)]
    prime_set = set(primes)

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        if n in prime_set:
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
