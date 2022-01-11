import sys
sys.stdin = open('input.txt')

N = str(sys.stdin.readline().rstrip())

print(N.zfill(4))