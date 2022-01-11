import sys
sys.stdin = open('input.txt', 'r')

N = int(sys.stdin.readline())
A = []
B = []
t = []
for _ in range(N):
    a, b = map(int, sys.stdin.readline().split())
    A.append(a)
    B.append(b)
    t.append(a/b)

ans = 0
left_t = sum(t)/2
left_line = 0
for i in range(N):
    if left_t - t[i] >= 0:
        left_t = left_t - t[i]
        ans += A[i]
        left_line = i
    else:
        break

if N == 1:
    print(A[0]/2)
else:
    if left_t > 0:
        ans += B[left_line+1]*left_t

    print(ans)