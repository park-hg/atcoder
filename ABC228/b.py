import sys
sys.stdin = open('input.txt', 'r')

N, X = map(int, sys.stdin.readline().split())
X -= 1
A = list(map(int, sys.stdin.readline().split()))
A = [a-1 for a in A]
l = [False]*N
l[X]= True

i = X
while True:
    if not l[A[i]]:
        l[A[i]] = True
        i = A[i]
    else:
        break

print(sum(l))