import sys
from collections import defaultdict, deque
sys.stdin = open('input.txt', 'r')

M = int(sys.stdin.readline())
graph = defaultdict(list)
for _ in range(M):
    u, v = map(int, sys.stdin.readline().split())
    u -= 1
    v -= 1
    graph[u].append(v)
    graph[v].append(u)
p = list(map(int, sys.stdin.readline().split()))
p = [i-1 for i in p]
position = [-1]*9
for i in range(len(p)):
    position[p[i]] = i

for i in range(9):
    if i not in p:
        start_v = i
        break

que = deque([start_v])
cnt = 0
visited = [False]*9
visited[start_v] = True

while que:
    v = que.popleft()
    print(v)
    if v == 8:
        if position[:-1] == list(range(8)):
            break
    
    for w in graph[v]:
        if not visited[w]:
            visited[w] = True
            position[v] = w
            position[w] = v
            print(position)
            que.append(w)
            cnt += 1
print(cnt)
