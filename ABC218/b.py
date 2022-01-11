import sys
sys.stdin = open('input.txt', 'r')

P = list(map(int, sys.stdin.readline().split()))
s = [chr(p+96) for p in P]
print(''.join(s))