import sys
sys.stdin = open('input.txt', 'r')
S = sys.stdin.readline().rstrip()
if S[-2:] == 'er':
    print('er')
elif S[-3:] == 'ist':
    print('ist')