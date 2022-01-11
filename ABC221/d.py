import sys
sys.stdin = open('input.txt', 'r')

N = int(sys.stdin.readline())

l = []
ans = [0]*N

for _ in range(N):
    A, B = map(int, sys.stdin.readline().split())
    l.append((A, 1))
    l.append((A+B, -1))

l.sort()

cnt = 0
for i in range(len(l)-1):
    cnt += l[i][1]
    if cnt > 0:
        ans[cnt-1] += l[i+1][0]-l[i][0]

print(*ans)
