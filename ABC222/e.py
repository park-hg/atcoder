import sys
from collections import defaultdict, deque

sys.stdin = open('input.txt', 'r')

N, M, K = map(int, sys.stdin.readline().split())
A = [i-1 for i in list(map(int, sys.stdin.readline().split()))]
graph = defaultdict(list)
edge = {}
for i in range(N-1):
    U, V = map(int, sys.stdin.readline().split())
    graph[V-1].append(U-1)
    graph[U-1].append(V-1)
    edge[(U-1, V-1)] = i
    edge[(V-1, U-1)] = i

c = [0]*(N-1)
def bfs(a, b):
    visited = [False]*N
    que = deque([[a, [a]]])

    while que:
        v, path = que.popleft()
        if v == b:
            return path
        for w in graph[v]:
            if not visited[w]:
                visited[w] = True
                que.append([w, path+[w]])


for i in range(M-1):
    path = bfs(A[i], A[i+1])
    for j in range(len(path)-1):
        c[edge[(path[j], path[j+1])]] += 1
c = [0] + c
S = sum(c)
dp = [[0]*((S+K)//2 + 1) for _ in range(N)]
for i in range(N):
    for j in range((S+K)//2 + 1):
        if i == 0 and j == 0:
            dp[i][j] = 1
        elif i >= 1 and j >= c[i]:
            dp[i][j] = (dp[i-1][j] + dp[i-1][j-c[i]]) % 998244353
        elif i >= 1:
            dp[i][j] = dp[i-1][j]

if S+K >= 0 and (S+K)%2 == 0:
    print(dp[-1][-1])
else:
    print(0)