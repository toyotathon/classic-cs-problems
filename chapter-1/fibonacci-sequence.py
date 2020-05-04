from typing import Dict
from functools import lru_cache

memo: Dict[int, int] = {0: 0, 1: 1}  # our base cases

# first given example of function
def recursive_fib(n: int) -> int:
    if n < 2:
        return n
    return recursive_fib(n - 1) + recursive_fib(n - 2)

# memoized example
def memo_fib(n: int) -> int:
    if n not in memo:
        memo[n] = memo_fib(n - 1) + memo_fib(n - 2)  # memoization
    return memo[n]


# same approach as first function, just using this decorator
@lru_cache(maxsize=None)
def auto_memo_fib(n: int) -> int:
    if n < 2:  # base case
        return n
    return auto_memo_fib(n - 2) + auto_memo_fib(n - 1)  # recursive case

# simple iterative approach
def iterative_fib(n: int) -> int:
    if n == 0:
        return n  # special case
    last: int = 0  # initially set to fib(0)
    next: int = 1  # initially set to fib(1)
    for _ in range(1, n):
        last, next = next, last + next
    return next

# creates a generator get fibonacci value
def fib_generator(n: int) -> int:
    yield 0  # special case
    if n > 0:
        yield 1  # special case
    last: int = 0  # initially set to fib(0)
    next: int = 1  # initially set to fib(1)
    for _ in range(1, n):
        last, next = next, last + next
        yield next  # main generation step


if __name__ == "__main__":
    print("recursive\t", recursive_fib(5))
    print("memoized\t", memo_fib(50))
    print("auto memoized\t", auto_memo_fib(50))
    print("iterative\t", iterative_fib(50))
    print("\n\n")
    for i in fib_generator(50):
        print("generator value\t", i)
