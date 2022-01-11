import sys
sys.stdin = open('input.txt', 'r')

s1 = sys.stdin.readline().rstrip()
s2 = sys.stdin.readline().rstrip()
s3 = sys.stdin.readline().rstrip()
T = sys.stdin.readline().rstrip()

ans = ''
for i in T:
    if i == '1':
        ans += s1
    elif i == '2':
        ans += s2
    elif i == '3':
        ans += s3

print(ans)