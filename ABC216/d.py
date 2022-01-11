import sys

sys.stdin = open('input.txt', 'r')
n, m = map(int, sys.stdin.readline().split())
a_list = []
for _ in range(m):
    k = int(sys.stdin.readline())
    a_list.append(list(map(int, sys.stdin.readline().split()))[::-1])

balls = {i:[] for i in range(1, n+1)}
pairs = []
for a in a_list:
    idx = a[-1]
    balls[idx].append(a)
    if len(balls[idx]) == 2:
        pairs.append(balls[idx])

removed_pairs = 0
while pairs:
    first, second = pairs.pop()
    first.pop()
    second.pop()
    removed_pairs += 1
    if first:
        idx = first[-1]
        balls[idx].append(first)
        if len(balls[idx]) == 2:
            pairs.append(balls[idx])
    if second:
        idx = second[-1]
        balls[idx].append(second)
        if len(balls[idx]) == 2:
            pairs.append(balls[idx])

if removed_pairs == n:
    print('Yes')
else:
    print('No')