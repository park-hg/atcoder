import sys
sys.stdin = open('input.txt', 'r')

N = int(sys.stdin.readline())
p = list(map(int, sys.stdin.readline().split()))
q = [0]*N

for i in range(N):
    q[p[i]-1] = i+1

print(*q)