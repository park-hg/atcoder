import sys
from collections import deque
import math

sys.stdin = open('input.txt')
N, M = map(int, sys.stdin.readline().split())

visited = [[-1]*N for _ in range(N)]
que = deque([[0, 0]])
visited[0][0] = 0

while que:
  k, l = que.popleft()
  for i in range(N):
    if M - (i-k)**2 >= 0:
      d = int(math.sqrt(M - (i-k)**2))
      if d**2 == M - (i-k)**2:
        if 0 <= l-d < N:
          if visited[i][l-d] == -1:
            visited[i][l-d] = visited[k][l] + 1
            que.append([i, l-d])
        if 0 <= l+d < N:
          if visited[i][l+d] == -1:
            visited[i][l+d] = visited[k][l] + 1
            que.append([i, l+d])

for row in visited:
  print(*row)