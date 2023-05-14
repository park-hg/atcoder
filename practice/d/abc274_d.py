import sys
sys.stdin = open('input.txt')

N, X, Y = map(int, sys.stdin.readline().split())
A = list(map(int, sys.stdin.readline().split()))
dpx = [set() for _ in range(N+1)]
dpy = [set() for _ in range(N+1)]
dpx[0].add(0)
dpx[1].add(A[0])
dpy[0].add(0)
dpy[1].add(0)

for i in range(1, N):
    if i%2 == 0:
        for x in dpx[i]:
            dpx[i+1].add(x+A[i])
            dpx[i+1].add(x-A[i])
        dpy[i+1] = dpy[i]
    else:
        for y in dpy[i]:
            dpy[i+1].add(y+A[i])
            dpy[i+1].add(y-A[i])
        dpx[i+1] = dpx[i]

if X in dpx[-1] and Y in dpy[-1]:
    print('Yes')
else:
    print('No')
