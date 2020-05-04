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


if __name__ == "__main__":
    print("recursive", recursive_fib(5))
    print("memoized", memo_fib(50))
    print("auto memoized (LRU cache)", auto_memo_fib(50))
