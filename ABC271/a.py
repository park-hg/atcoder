import sys
sys.stdin = open('input.txt')

N = int(sys.stdin.readline())

ans = ''
while N:
  N, r = divmod(N, 16)
  if r == 10:
    ans += 'A'
  elif r == 11:
    ans += 'B'
  elif r == 12:
    ans += 'C'
  elif r == 13:
    ans += 'D'
  elif r == 14:
    ans += 'E'
  elif r == 15:
    ans += 'F'
  else:
    ans += str(r)

print(ans[::-1].zfill(2))