import collections
import sys
sys.setrecursionlimit(10000)

n, m = map(int, input().split())
graph = collections.defaultdict(list)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

def dfs(v, temp):
    if temp[v-1]:
        return
    temp[v-1] = True
    for w in graph[v]:
        dfs(w, temp)

ans = 0
for i in range(1,n+1):
    temp = [False] * n
    dfs(i, temp)
    ans += sum(temp)
print(ans)