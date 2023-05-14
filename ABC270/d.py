import sys
sys.stdin = open('input.txt')

N, K = map(int, sys.stdin.readline().split())
A = list(map(int, sys.stdin.readline().split()))

dp = [0]*(N+1)
m = len(A)
for i in range(N+1):
  for j in range(m):
    if A[j] <= i:
      dp[i] = max(dp[i], A[j]+ (i-A[j]) - dp[i-A[j]])
    else:
      break

print(dp[-1])