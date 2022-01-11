import sys
sys.stdin = open('input.txt', 'r')

X = int(sys.stdin.readline())

if X > 0 and X%100 == 0:
    print('Yes')
else:
    print('No')