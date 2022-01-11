import sys
from fractions import Fraction
sys.stdin = open('input.txt', 'r')

N = int(sys.stdin.readline())
grid = []
for _ in range(N):
    grid.append(list(sys.stdin.readline().rstrip()))
S = []
for i in range(N):
    for j in range(N):
        if grid[i][j] == '#':
            S.append([i, j])
grid = []
for _ in range(N):
    grid.append(list(sys.stdin.readline().rstrip()))
T = []
for i in range(N):
    for j in range(N):
        if grid[i][j] == '#':
            T.append([i, j])

def move(s):
    a, b = 0, 0
    for x, y in s:
        a += x
        b += y
    a = Fraction(a, len(s))
    b = Fraction(b, len(s))
    ss = []
    for x, y in s:
        ss.append([x-a, y-b])
    return ss

def rotate(s):
    ss = []
    for x, y in s:
        ss.append([-y, x])
    return ss

S = move(S)
T = move(T)
T.sort()

for i in range(4):
    S.sort()
    if S == T:
        print('Yes')
        exit()
    else:
        S = rotate(S)
print('No')