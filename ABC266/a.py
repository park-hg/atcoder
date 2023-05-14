import sys
sys.stdin = open('input.txt')
S = sys.stdin.readline().rstrip()
print(S[len(S)//2])