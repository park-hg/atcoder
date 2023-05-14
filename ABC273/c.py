import sys
import bisect
from collections import Counter

sys.stdin = open('input.txt')

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
A_set = list(set(A))
A_set.sort()

ans = 0
B = []
for i in range(1, N+1):
    B.append(len(A_set)-bisect.bisect(A_set, A[i-1]))

counter = Counter(B)

for i in range(N):
    if i in counter:
        print(counter[i])
    else:
        print(0)