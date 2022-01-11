import sys
from itertools import combinations
sys.stdin = open('input.txt', 'r')

N = int(sys.stdin.readline())
p = []
for _ in range(N):
    p.append(list(map(int, sys.stdin.readline().split())))


ans = 0
for x, y, z in combinations(p, 3):
    if x[0]*y[1]+y[0]*z[1]+z[0]*x[1] != x[1]*y[0]+y[1]*z[0]+z[1]*x[0]:
        ans += 1
print(ans)