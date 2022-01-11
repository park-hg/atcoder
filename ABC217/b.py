import sys
sys.stdin = open('input.txt', 'r')

l = ['ABC', 'ARC', 'AGC', 'AHC']
ll = []
for _ in range(3):
    l.remove(sys.stdin.readline().rstrip())

print(*l)