import sys

sys.stdin = open('input.txt')
S = sys.stdin.readline().strip()
N = int(sys.stdin.readline().strip())
N = bin(N)[2:]

if len(S) > len(N):
    N = "0"*(len(S)-len(N)) + N
elif len(S) < len(N):
    S = "0"*(len(N)-len(S)) + S

S = list(S)
answer = []
for i in range(len(S)):
    if S[i] == "?":
        temp = S[:i] + ["1"] + S[i+1:]
        temp = "".join(temp)
        temp = temp.replace("?", "0")
        if int(temp, 2) <= int(N, 2):
            S[i] = "1"
        else:
            S[i] = "0"

result = int("".join(S), 2)
if result > int(N, 2):
    print(-1)
else:
    print(result)