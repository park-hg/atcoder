import sys
sys.stdin = open('input.txt')
N = int(sys.stdin.readline())
info = []
max_T = 0
for _ in range(N):
  T, X, a = map(int, sys.stdin.readline().split())
  max_T = max(max_T, T)
  info.append((T, X, a))

A = [[0, 0, 0, 0, 0] for _ in range(max_T+1)]
for T, X, a in info:
  A[T][X] = a

dp = [[-10**18]*5 for _ in range(max_T+1)]
dp[0][0] = A[0][0]

for t in range(max_T):
  for x in range(5):
    if x == 0:
      dp[t+1][x] = max(dp[t][x], dp[t][x+1]) + A[t+1][x]
    elif x == 4:
      dp[t+1][x] = max(dp[t][x-1], dp[t][x]) + A[t+1][x]
    else:
      dp[t+1][x] = max(dp[t][x-1], dp[t][x], dp[t][x+1]) + A[t+1][x]

  print(dp)
  print()
