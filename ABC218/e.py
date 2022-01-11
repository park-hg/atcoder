from collections import defaultdict
import sys
import heapq

sys.stdin = open('input.txt', 'r')
N, M = map(int, sys.stdin.readline().split())
graph = defaultdict(list)
ans = 0
for _ in range(M):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a-1].append([c, a-1, b-1])
    graph[b-1].append([c, b-1, a-1])
    if c > 0:
        ans += c

visited = [False] * N
visited[0] = True
heap = graph[0]
heapq.heapify(heap)
while heap:
    cost, u, v = heapq.heappop(heap)
    if not visited[v]:
        if cost > 0:
            ans -= cost
        visited[v] = True
        for edge in graph[v]:
            if not visited[edge[2]]:
                heapq.heappush(heap, edge)
print(ans)