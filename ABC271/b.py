import sys
sys.stdin = open('input.txt')

N, Q = map(int, sys.stdin.readline().split())
A = []
for _ in range(N):
  a = list(map(int, sys.stdin.readline().split()))
  A.append(a[1:])

for _ in range(Q):
  s, t = map(int, sys.stdin.readline().split())
  print(A[s-1][t-1])