import sys
sys.stdin = open('input.txt')
H, W = map(int, sys.stdin.readline().split())
grid = [list(sys.stdin.readline().rstrip()) for _ in range(H)]

# dp[i][j]: (i, j)에 있을 때 (i+j)가 짝수이면 게임종료까지 (타카하시 - 아오키)의 최대값, (i+j)가 짝수이면 최소값.
# dp[i][j] = (if (i+j)%2 == 0) max(dp[i+1][j] + f(i+1, j), dp[i][j+1] + f(i, j+1))
# dp[i][j] = (else) min(dp[i+1][j] - f(i+1, j), dp[i][j+1] - f(i, j+1))

def func(i, j):
  if grid[i][j] == '+':
    return 1
  return -1

dp = [[0]*W for _ in range(H)]
for i in range(H-1, -1, -1):
  for j in range(W-1, -1, -1):
    if i == H-1 and j == W-1:
      continue

    if (i+j)%2 == 0:
      dp[i][j] = -10**18
      if i+1 <= H-1:
        dp[i][j] = max(dp[i][j], dp[i+1][j]+func(i+1, j))
      if j+1 <= W-1:
        dp[i][j] = max(dp[i][j], dp[i][j+1]+func(i, j+1))
    else:
      dp[i][j] = 10**18
      if i+1 <= H-1:
        dp[i][j] = min(dp[i][j], dp[i+1][j]-func(i+1, j))
      if j+1 <= W-1:
        dp[i][j] = min(dp[i][j], dp[i][j+1]-func(i, j+1))

if dp[0][0] > 0:
  print('Takahashi')
elif dp[i][0] < 0:
  print('Aoki')
else:
  print('Draw')