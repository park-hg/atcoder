import sys
from collections import Counter
sys.stdin = open('input.txt', 'r')

N, K = map(int, sys.stdin.readline().split())

P = []
for _ in range(N):
    P.append(sum(list(map(int, sys.stdin.readline().split()))))
P_cnt = Counter(P)
i = 1
for score in sorted(P_cnt, reverse=True):
    if i <= K:
        kth = score
    else:
        break
    i += P_cnt[score]
for i in range(N):
    if P[i] + 300 >= kth:
        print('Yes')
    else:
        print('No')