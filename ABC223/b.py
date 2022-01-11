import sys
sys.stdin = open('input.txt', 'r')

S = sys.stdin.readline().rstrip()

min_S = S
max_S = S

for i in range(len(S)):
    S = S[1:] + S[0]
    if min_S > S:
        min_S = S
    if max_S < S:
        max_S = S

S = S[1:] + S[0]

for i in range(len(S)):
    S = S[-1] + S[:-1]
    if min_S > S:
        min_S = S
    if max_S < S:
        max_S = S

print(min_S)
print(max_S)    
