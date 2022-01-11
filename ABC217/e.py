import sys
from collections import deque
import heapq
sys.stdin = open('input.txt', 'r')

Q = int(sys.stdin.readline())
que = deque([])
heap = []
for _ in range(Q):
    f = sys.stdin.readline().split()
    c = int(f[0])
    if c == 1:
        x = int(f[1])
        que.append(x)
    elif c == 2:
        if heap:
            ans = heapq.heappop(heap)
        else:
            ans = que.popleft()
        print(ans)
    else:
        while que:
            heapq.heappush(heap, que.popleft())