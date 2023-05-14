import sys
sys.stdin = open('input.txt')
N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
print(sum(A))