import sys
sys.stdin = open('input.txt')
H, W = map(int, sys.stdin.readline().split())
grid = [list(sys.stdin.readline().rstrip()) for _ in range(H)]

s = {'+':1, '-':-1}

dp = [[-10**18]*W for _ in range(H)]

for i in range(H-1, -1, -1):
  for j in range(W-1, -1, -1):
    if i == H-1 and j == W-1:
      dp[i][j] = 0
      continue
    
    if i+1 <= H-1:
      dp[i][j] = max(dp[i][j], s[grid[i+1][j]]-dp[i+1][j])
    if j+1 <= W-1:
      dp[i][j] = max(dp[i][j], s[grid[i][j+1]]-dp[i][j+1])

if dp[0][0] > 0:
  print('Takahashi')
elif dp[0][0] < 0:
  print('Aoki')
else:
  print('Draw')

