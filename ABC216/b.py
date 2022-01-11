import sys

sys.stdin = open('input.txt', 'r')

N = int(sys.stdin.readline())
name = []
for _ in range(N):
    n = sys.stdin.readline()
    if n in name:
        print('Yes')
        exit()
    else:
        name.append(n)

print('No')