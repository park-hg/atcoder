import sys
import bisect
import array

sys.stdin = open('input.txt', 'r')

L, Q = map(int, sys.stdin.readline().split())
l = array.array('i', [0, L])

for _ in range(Q):
    c, x = map(int, sys.stdin.readline().split())
    idx = bisect.bisect_left(l, x)
    if c == 1:
        l.insert(idx, x)
    else:
        print(l[idx]-l[idx-1])