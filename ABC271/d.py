import sys
sys.stdin = open('input.txt')
N, S = map(int, sys.stdin.readline().split())

a, b = [], []
for _ in range(N):
  aa, bb = map(int, sys.stdin.readline().split())
  a.append(aa)
  b.append(bb)


dp = [[False]*(S+1) for _ in range(N+1)]
dp[0][0] = ''

for i in range(N):
  for j in range(S+1):
    if j >= a[i]:
      if dp[i][j-a[i]] != False:
        dp[i+1][j] = dp[i][j-a[i]]+'H'
    if j >= b[i]:
      if dp[i][j-b[i]] != False:
        dp[i+1][j] = dp[i][j-b[i]]+'T'

if dp[-1][-1]:
  print('Yes')
  print(dp[-1][-1])
else:
  print('No')