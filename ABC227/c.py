import sys
sys.stdin = open('input.txt', 'r')

N = int(sys.stdin.readline())

i = 1
ans = 0

while i*i*i <= N:
    M = N//i
    j = i

    while j*j <= M:
        ans += (M//j - j + 1)
        j += 1
    i += 1

print(ans)