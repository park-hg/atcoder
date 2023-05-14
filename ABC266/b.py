import sys
sys.stdin = open('input.txt')
N = int(sys.stdin.readline())
m = (998244353-N)//998244353
print((m*998244353 + N)%998244353)