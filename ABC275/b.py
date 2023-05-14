import sys
sys.stdin = open('input.txt')
A, B, C, D, E, F = map(int, sys.stdin.readline().split())

print((A*B*C-D*E*F) % 998244353)