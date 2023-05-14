import sys
from collections import defaultdict
from itertools import combinations
sys.stdin = open('input.txt')
N, M = map(int, sys.stdin.readline().split())

d = defaultdict(set)
for i in range(M):
  query = list(map(int, sys.stdin.readline().split()))
  k, x = query[0], query[1:]
  for p in x:
    d[p-1].add(i)

def check():
  for i, j in combinations(range(N), 2):
    if len(d[i].intersection(d[j])) == 0:
      return False
  return True

if check():
  print('Yes')
else:
  print('No')
