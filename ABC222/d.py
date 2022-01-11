import sys
sys.stdin = open('input.txt', 'r')

N = int(sys.stdin.readline())

a = list(map(int, sys.stdin.readline().split()))
b = list(map(int, sys.stdin.readline().split()))

M = max(max(a), max(b))

dp = [[0]*(M+1) for _ in range(N+1)]

for i in range(N+1):
    for j in range(M+1):
        if i == 0 and j == 0:
            dp[i][j] = 1
        elif i >= 1 and a[i-1] <= j <= b[i-1]:
            dp[i][j] = (dp[i-1][j] + dp[i][j-1]) % 998244353
        else:
            dp[i][j] = dp[i][j-1]

print(dp[-1][-1])