import sys

sys.stdin = open('input.txt', 'r')

X = sys.stdin.readline().rstrip()
N = int(sys.stdin.readline())
l = []
for _ in range(N):
    S = sys.stdin.readline().rstrip()
    order = []
    for chr in S:
        order.append(X.index(chr))
    l.append((S, order))
print(l)
l.sort(key=lambda x:x[1])
for name, _ in l:
    print(name)