#!/usr/bin/python3
"""Compute the minimum operations needed to produce ``n`` H characters."""


def minOperations(n):
    """Return the fewest Copy All and Paste operations needed to reach n.

    Each prime factor of n contributes that many operations: copy the current
    content once, then paste it enough times to multiply the character count
    by that factor.
    """
    if n <= 1:
        return 0

    operations = 0
    divisor = 2
    while divisor * divisor <= n:
        while n % divisor == 0:
            operations += divisor
            n //= divisor
        divisor += 1

    if n > 1:
        operations += n

    return operations
