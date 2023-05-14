import sys
from functools import lru_cache
sys.stdin = open('input.txt')

N = int(sys.stdin.readline())

@lru_cache(None)
def func(n):
    if n == 0:
        return 1

    return func(n//2) + func(n//3)


print(func(10**18))