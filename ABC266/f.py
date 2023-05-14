import sys
from collections import defaultdict, deque
sys.stdin = open('input.txt')
N = int(sys.stdin.readline())
edges = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

graph = defaultdict(list)
degree = [0]*(N+1)
for u, v in edges:
  graph[u].append(v)
  graph[v].append(u)
  degree[u] += 1
  degree[v] += 1

que = deque()
for i in range(N+1):
  if degree[i] == 1:
    que.append(i)

while que:
  v = que.popleft()
  for u in graph[v]:
    degree[u] -= 1
    if degree[u] == 1:
      que.append(u)
  degree[v] -= 1

root = [-1]*(N+1)
for i in range(1, N+1):
  if degree[i] > 0:
    root[i] = i

def bfs(s):
  que = deque([s])
  while que:
    v = que.popleft()
    for w in graph[v]:
      if root[w] == -1:
        root[w] = s
        que.append(w)

for i in range(1, N+1):
  if degree[i] > 0:
    bfs(i)

Q = int(sys.stdin.readline())
queries = [list(map(int, sys.stdin.readline().split())) for _ in range(Q)]
for a, b in queries:
  if root[a] == root[b]:
    print('Yes')
  else:
    print('No')
