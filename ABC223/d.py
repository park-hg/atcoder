import sys
from collections import defaultdict
import heapq

sys.stdin = open('input.txt', 'r')
N, M = map(int, sys.stdin.readline().split())
graph = defaultdict(list)
for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)

indegree = {i:0 for i in range(1, N+1)}
for v in indegree:
    for u in graph[v]:
        indegree[u] += 1

heap = []
for i in range(1, N+1):
    if indegree[i] == 0:
        heapq.heappush(heap, i)

ans = []
while heap:
    v = heapq.heappop(heap)
    for u in graph[v]:
        indegree[u] -= 1
        if indegree[u] == 0:
            heapq.heappush(heap, u)
    graph.pop(v)
    ans.append(v)

if graph:
    print(-1)
else:
    print(*ans)