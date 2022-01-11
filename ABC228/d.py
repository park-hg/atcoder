import sys

N = 1<<20
A = [-1]*N
par = [-1]*N
Q = int(sys.stdin.readline())

def find(x):
    if par[x] == -1:
        return x
    par[x] = find(par[x])
    return par[x]
    
def unite(x, y):
    x, y = find(x), find(y)
    if x == y:
        return
    par[x] = y

for _ in range(Q):
    t, x = map(int, sys.stdin.readline().split())
    h = x%N
    if t == 1:
        A[find(h)] = x
        unite(find(h), (find(h)+1)%N)
    else:
        print(A[h])