# Minimum Operations

`0-minoperations.py` provides `minOperations(n)`, which returns the minimum
number of `Copy All` and `Paste` operations needed to create exactly `n`
`H` characters from one initial `H`. It returns `0` for values below `2`.

The solution factors `n` into primes and sums those factors, counting
multiplicity. For example, `12 = 2 * 2 * 3`, so reaching 12 characters takes
`2 + 2 + 3 = 7` operations.
