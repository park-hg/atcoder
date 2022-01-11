import sys
sys.stdin = open('input.txt', 'r')

N, K = map(int, sys.stdin.readline().split())
A = list(map(int, sys.stdin.readline().split()))


def func(x):
    y = 0
    for a in A:
        y += min(a, x)
    return y

lo, hi = 0, sum(A)+1
while lo < hi:
    mid = (lo + hi) // 2
    if func(mid) >= K*mid:
        lo = mid+1
    else:
        hi = mid

print(lo-1)