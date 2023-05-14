import sys
from collections import defaultdict, deque
sys.stdin = open('input.txt')

N, X, Y = map(int, sys.stdin.readline().split())
graph = defaultdict(list)
for _ in range(N-1):
  U, V = map(int, sys.stdin.readline().split())
  graph[U].append(V)
  graph[V].append(U)

que = deque([X])
visited = [None]*(N+1)
visited[X] = -1
while que:
  v = que.popleft()
  if v == Y:
    break

  for w in graph[v]:
    if visited[w] is None:
      visited[w] = v
      que.append(w)

cur = Y
path = []
while cur != -1:
  path.append(cur)
  cur = visited[cur]

print(*path[::-1])