import sys
sys.stdin = open('input.txt', 'r')

n, Q = map(int, sys.stdin.readline().split())
s = sys.stdin.readline()

table = {')':'('}
stack = []

def check(s):
    for char in s_test:
        if char not in table:
            stack.append(char)
        elif not stack or table[char] != stack.pop():
            return False
    return len(stack) == 0

for _ in range(Q):
    q, l, r = map(int, sys.stdin.readline().split())
    l -= 1
    r -= 1
    if q == 1:
        s = s[:l] + s[r] + s[l+1:r] + s[l] + s[r+1:]
    elif q == 2:
        s_test = s[l:r+1]
        if check(s_test):
            print('Yes')
        else:
            print('No')

