import sys
from bisect import bisect
sys.stdin = open('input.txt')

H, W, x, y = map(int, sys.stdin.readline().split())
N = int(sys.stdin.readline())
wall_x = {}
wall_y = {}
for _ in range(N):
    r, c = map(int, sys.stdin.readline().split())
    if r in wall_x:
        wall_x[r].append(c)
    else:
        wall_x[r] = [0, c, W+1]
    if c in wall_y:
        wall_y[c].append(r)
    else:
        wall_y[c] = [0, r, H+1]

for r in wall_x:
    wall_x[r].sort()

for c in wall_y:
    wall_y[c].sort()

Q = int(sys.stdin.readline())
for _ in range(Q):
    d, l = sys.stdin.readline().split()
    l = int(l)
    if d == 'L':
        if x not in wall_x:
            y = max(1, y-l)
        else:
            idx = bisect(wall_x[x], y)
            y = max(wall_x[x][idx-1] + 1, y-l)
    elif d == 'R':
        if x not in wall_x:
            y = min(W, y+l)
        else:
            idx = bisect(wall_x[x], y)
            y = min(wall_x[x][idx] - 1, y+l)
    elif d == 'U':
        if y not in wall_y:
            x = max(1, x-l)
        else:
            idx = bisect(wall_y[y], x)
            x = max(wall_y[y][idx-1] + 1, x-l)
    elif d == 'D':
        if y not in wall_y:
            x = min(H, x+l)
        else:
            idx = bisect(wall_y[y], x)
            x = min(wall_y[y][idx] - 1, x+l)

    print(x, y)

