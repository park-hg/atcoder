import sys
sys.stdin = open('input.txt')
N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))

odds, evens = [], []
for a in A:
  if a%2 == 0:
    evens.append(a)
  else:
    odds.append(a)

evens.sort()
odds.sort()
if len(evens) < 2 and len(odds) < 2:
  print(-1)
else:
  print(max(sum(evens[-2:]), sum(odds[-2:])))