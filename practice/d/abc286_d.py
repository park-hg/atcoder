import sys
sys.stdin = open('input.txt')

N, X = map(int, sys.stdin.readline().split())

coins = []
for _ in range(N):
    A, B = map(int, sys.stdin.readline().split())
    for _ in range(B):
        coins.append(A)

dp = [[False]*(X+1) for _ in range(len(coins)+1)]

dp[0][0] = True

for i in range(1, len(coins)+1):
    for j in range(X+1):
        dp[i][j] = dp[i-1][j]
        if j >= coins[i-1]:
            dp[i][j] |= dp[i-1][j-coins[i-1]]

if dp[-1][-1]:
    print('Yes')
else:
    print('No')