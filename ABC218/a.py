import sys
sys.stdin = open('input.txt')
N = int(sys.stdin.readline())
S = sys.stdin.readline().rstrip()

if S[N-1] == 'o':
    print('Yes')
else:
    print('No')