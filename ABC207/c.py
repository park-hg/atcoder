import sys

sys.stdin = open("input.txt", "r")

n = int(sys.stdin.readline())


intervals = []
for _ in range(n):
    t, l, r = map(int, sys.stdin.readline().split())
    if t == 2:
        r -= 0.1
    elif t == 3:
        l += 0.1
    elif t == 4:
        l += 0.1
        r -= 0.1
    intervals.append((l, r))

ans = 0
for i in range(n):
    for j in range(i+1, n):
        a, b = intervals[i]
        c, d = intervals[j]
        if not(b < c or d < a):
            ans += 1
print(ans)