import sys
sys.stdin = open('input.txt')

N = int(sys.stdin.readline())

def func(x):
    if x == 0:
        return 1

    return x * func(x-1)

print(func(N))