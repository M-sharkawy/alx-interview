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
    if not nums or x < 1:
        return None

    max_n = max(nums)

    is_prime = [True] * (max_n + 1)
    is_prime[0:2] = [False, False]
    for i in range(2, int(max_n ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, max_n + 1, i):
                is_prime[j] = False

    prime_count_up_to = [0] * (max_n + 1)
    count = 0
    for i in range(1, max_n + 1):
        if is_prime[i]:
            count += 1
        prime_count_up_to[i] = count

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        if prime_count_up_to[n] % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
