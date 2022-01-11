import sys
sys.stdin = open('input.txt', 'r')

S, T, X = map(int, sys.stdin.readline().split())

if S < T:
    if S <= X < T:
        print('Yes')
    else:
        print('No')
else:
    if S <= X or X < T:
        print('Yes')
    else:
        print('No')