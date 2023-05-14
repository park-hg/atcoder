import sys
sys.stdin = open('input.txt')

N = int(sys.stdin.readline())
H = list(map(int, sys.stdin.readline().split()))

ans = -1
max_h = 0
for i in range(N):
    if H[i] > max_h:
        ans = i
        max_h = H[i]
print(ans+1)
