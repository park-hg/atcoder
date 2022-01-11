import sys
sys.stdin = open('input.txt', 'r')

N, P = map(int, sys.stdin.readline().split())

a = list(map(int, sys.stdin.readline().split()))

cnt = 0
for i in a:
    if i < P:
        cnt += 1

print(cnt)