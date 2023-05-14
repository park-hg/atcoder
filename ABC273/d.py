import sys
import bisect
sys.stdin = open('input.txt')

H, W, x, y = map(int, sys.stdin.readline().split())
N = int(sys.stdin.readline())
wall_x = {}
wall_y = {}
for _ in range(N):
    r, c = map(int, sys.stdin.readline().split())
    if c not in wall_x:
        wall_x[c] = [0, r]
    else:
        wall_x[c].append(r)

    if r not in wall_y:
        wall_y[r] = [0, c]
    else:
        wall_y[r].append(c)

for c in wall_x:
    wall_x[c].append(W+1)
    wall_x[c].sort()

for r in wall_y:
    wall_y[r].append(H+1)
    wall_y[r].sort()

# print(wall_x)
# print(wall_y)

Q = int(sys.stdin.readline())
for _ in range(Q):
    d, l = sys.stdin.readline().split()
    l = int(l)
    if d == 'L':
        if x in wall_y:
            next_wall_idx = bisect.bisect(wall_y[x], y)-1
            # print(wall_y[x][next_wall_idx])
            y = max(wall_y[x][next_wall_idx]+1, y-l)
        else:
            y = max(1, y-l)
    elif d == 'R':
        if x in wall_y:
            next_wall_idx = bisect.bisect(wall_y[x], y)
            # print(wall_y[x][next_wall_idx])
            y = min(wall_y[x][next_wall_idx]-1, y+l)
        else:
            y = min(W, y+l)
    elif d == 'D':
        if y in wall_x:
            next_wall_idx = bisect.bisect(wall_x[y], x)
            # print(wall_x[y], wall_x[y][next_wall_idx])
            x = min(wall_x[y][next_wall_idx]-1, x+l)
        else:
            x = min(H, x+l)
    elif d == 'U':
        if y in wall_x:
            next_wall_idx = bisect.bisect(wall_x[y], x)-1
            # print(wall_x[y], wall_x[y][next_wall_idx])
            x = max(wall_x[y][next_wall_idx]+1, x-l)
        else:
            x = max(1, x-l)

    print(x, y)
    
l = [0, 2, 5, 10, 11]

print(bisect.bisect(l, 1)-1)




    