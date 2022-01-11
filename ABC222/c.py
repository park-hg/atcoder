import sys
sys.stdin = open('input.txt', 'r')

N, M = map(int, sys.stdin.readline().split())
A = []
for _ in range(2*N):
    A.append(list(sys.stdin.readline().rstrip()))

l = [[-i, 0] for i in range(2*N)]

for round in range(M):
    for k in range(0, 2*N, 2):
        if A[-l[k][0]][round] == 'G':
            if A[-l[k+1][0]][round] == 'C':
                l[k][1] += 1
            elif A[-l[k+1][0]][round] == 'P':
                l[k+1][1] += 1
        elif A[-l[k][0]][round] == 'C':
            if A[-l[k+1][0]][round] == 'P':
                l[k][1] += 1
            elif A[-l[k+1][0]][round] == 'G':
                l[k+1][1] += 1
        elif A[-l[k][0]][round] == 'P':
            if A[-l[k+1][0]][round] == 'G':
                l[k][1] += 1
            elif A[-l[k+1][0]][round] == 'C':
                l[k+1][1] += 1
    l.sort(key=lambda x: (x[1], x[0]), reverse=True)

for i, _ in l:
    print(-i+1)