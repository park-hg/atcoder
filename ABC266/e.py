import sys
sys.stdin = open('input.txt')
N = int(sys.stdin.readline())

dp = [0]*(N+1)
dp[1] = 3.5

for i in range(2, N+1):
  for k in range(1, 7):
    dp[i] += max(k, dp[i-1])/6.0

print(dp[-1])