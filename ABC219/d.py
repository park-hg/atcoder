import sys
from array import array
sys.stdin = open('input.txt', 'r')

N = int(sys.stdin.readline())
X ,Y = map(int, sys.stdin.readline().split())
l = []
for _ in range(N):
    arr = array('l', list(map(int, sys.stdin.readline().split())))
    l.append(arr)

dp = [[array('l', [301]*(Y+1)) for _ in range(X+1)] for _ in range(N+1)]
dp[0][0][0] = 0

for i in range(N):
    for j in range(X+1):
        jj = min(j+l[i][0], X)
        for k in range(Y+1):
            kk = min(k+l[i][1], Y)
            dp[i+1][jj][kk] = min(dp[i+1][jj][kk], dp[i][j][k]+1)
            dp[i+1][j][k] = min(dp[i+1][j][k], dp[i][j][k])

if dp[-1][-1][-1] == 301:
    print(-1)
else:
    print(dp[-1][-1][-1])