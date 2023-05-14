import sys
sys.stdin = open('input.txt')

X, Y, Z = map(int, sys.stdin.readline().split())

if 0 < Y < Z:
  if X < Y:
    print(abs(X))
  else:
    print(-1)
elif 0 < Z < Y:
  print(abs(X))
elif Y < 0 < Z:
  if X < Y:
    print(Z*2 + abs(X))
  else:
    print(abs(X))
elif Y < Z < 0:
  print(abs(X))
elif Z < 0 < Y:
  if X < Y:
    print(abs(X))
  else:
    print(abs(Z)*2 + X)
elif Z < Y < 0:
  if X < Y:
    print(-1)
  else:
    print(abs(X))