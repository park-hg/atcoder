import sys

sys.stdin = open('input.txt', 'r')

X, Y = map(int, sys.stdin.readline().split('.'))
if 0 <= Y <= 2:
    print(f"{X}-")
elif 3 <= Y <= 6:
    print(X)
else:
    print(f"{X}+")