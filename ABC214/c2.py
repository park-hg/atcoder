import sys
import heapq

sys.stdin = open('input.txt', 'r')

n = int(sys.stdin.readline())
s = list(map(int, sys.stdin.readline().split()))
t = list(map(int, sys.stdin.readline().split()))

graph = {}
for i in range(n+1):
    if i == 0:
        graph[0] = {k:v for k, v in enumerate(t, start=1)}
    else:
        graph[i] = {(i%n+1):s[i-1]}

distance = [1000000001] * (n+1)
distance[0] = 0

heap = [(0, 0)]
while heap:
    v, dist = heapq.heappop(heap)
    if distance[v] < dist:
        continue
    for w in graph[v]:
        if distance[w] < dist + graph[v][w]:
            continue
        else:
            distance[w] = dist + graph[v][w]
            heapq.heappush(heap, (w, distance[w]))
    
for ans in distance[1:]:
    print(ans)