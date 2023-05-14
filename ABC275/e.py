import sys
sys.stdin = open('input.txt')

N, M, K = map(int, sys.stdin.readline().split())
mod = 998244353
inv_mod = pow(M, mod-2, mod) % mod
dp = [[0]*(N+1) for _ in range(K+1)]

dp[0][0] = 1

for i in range(K):
    for j in range(N+1):
        if j == N:
            dp[i+1][j] += dp[i][j]
            continue
        for m in range(1, M+1):
            if j+m <= N:
                dp[i+1][j+m] += dp[i][j]*inv_mod
                dp[i+1][j+m] %= mod
            else:
                dp[i+1][2*N-j-m] += dp[i][j]*inv_mod
                dp[i+1][2*N-j-m] %= mod

print(dp[-1][-1]%mod)
