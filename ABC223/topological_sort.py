"""
https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=GRL_4_B&lang=ja
"""

import sys
from collections import defaultdict, deque
sys.stdin = open('input.txt', 'r')

V, E = map(int, sys.stdin.readline().split())
G = defaultdict(list)
for _ in range(E):
    s, t = map(int, sys.stdin.readline().split())
    G[s].append(t)

que = deque()
result = []
indegree = [0]*V
for v in range(V):
    for u in G[v]:
        indegree[u] += 1

for v in range(V):
    if indegree[v] == 0:
        que.append(v)

while que:
    v = que.popleft()
    result.append(v)
    for u in G[v]:
        indegree[u] -= 1
        if indegree[u] == 0:
            que.append(u)
    G.pop(v)

for v in result:
    print(v)