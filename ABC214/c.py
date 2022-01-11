import sys

sys.stdin = open('input.txt', 'r')

n = int(sys.stdin.readline())
s = list(map(int, sys.stdin.readline().split()))
t = list(map(int, sys.stdin.readline().split()))
#sys.stdin.buffer.readline()


for i in range(n):
    t[i] = min(t[i], t[i-1] + s[i-1])
for i in range(n):
    t[i] = min(t[i], t[i-1] + s[i-1])

for i in t:
    print(i)