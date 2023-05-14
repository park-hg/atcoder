import sys
from itertools import combinations
sys.stdin = open('input.txt')

points = []
for i in range(9):
    S = list(sys.stdin.readline().rstrip())
    for j in range(9):
        if S[j] == '#':
            points.append((i+1, j+1))


def dist(p1, p2):
    return (p1[0]-p2[0])**2 + (p1[1]-p2[1])**2

def is_square(p1, p2, p3, p4):
    d2, d3, d4 = dist(p1, p2), dist(p1, p3), dist(p1, p4)

    if d2 == 0 or d3 == 0 or d4 == 0:
        return False

    if d2 == d3 and 2 * d2 == d4:
        if dist(p2, p4) == dist(p3, p4) == d2 == d3:
            return True

    if d3 == d4 and 2 * d3 == d2:
        if dist(p2, p3) == dist(p2, p4) == d3 == d4:
            return True

    if d2 == d4 and 2 * d2 == d3:
        if dist(p2, p3) == dist(p3, p4) == d2 == d4:
            return True

    return False

ans = 0
for comb in combinations(points, 4):
    if is_square(*comb):
        ans += 1
print(ans)
