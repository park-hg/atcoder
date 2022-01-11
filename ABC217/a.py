import sys
sys.stdin = open('input.txt')
a, b = sys.stdin.readline().split()
if a < b:
    print('Yes')
else:
    print('No')