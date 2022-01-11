import sys
sys.stdin = open('input.txt', 'r')

N = int(sys.stdin.readline())
S = list(map(int, sys.stdin.readline().split()))

l = []
for i in range(1, 143):
    for j in range(1, 143):
        l.append(4*i*j + 3*i + 3*j)

ans = 0
for s in S:
    if s not in l:
        ans += 1
print(ans)