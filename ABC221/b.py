import sys
sys.stdin = open('input.txt', 'r')

S = sys.stdin.readline().rstrip()
T = sys.stdin.readline().rstrip()

if S == T:
    print('Yes')
    exit()

for i in range(len(S)-1):
    S_new = S[:i]+S[i+1]+S[i]+S[i+2:]
    if S_new == T:
        print('Yes')
        exit()

print('No')