import sys

sys.stdin = open('input.txt', 'r')

N = int(sys.stdin.readline())

p = []
s = set()
for _ in range(N):
    x, y = map(int, sys.stdin.readline().split())
    p.append((x, y))
    s.add((x, y))

ans = 0
for i in range(N-1):
    for j in range(i+1, N):
        x1, y1 = p[i]
        x2, y2 = p[j]
        if x1 != x2 and y1 != y2:
            if (x1, y2) in s and (x2, y1) in s:
                ans += 1
print(ans//2)