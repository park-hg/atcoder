import sys
sys.stdin = open('input.txt', 'r')

N, K, A = map(int, sys.stdin.readline().split())

if K < N-A+1:
    print(A+K-1)
else:
    K -= N-A+1
    if K%N == 0:
        print(N)
    else:
        print(K%N)