import sys
sys.stdin = open('input.txt')
A, B = map(int, sys.stdin.readline().split())

print(A|B)