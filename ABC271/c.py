import sys
sys.stdin = open('input.txt')

N = int(sys.stdin.readline())
vis = [False]*(N+1)
cnt = 0
for i in map(int, sys.stdin.readline().split()):
  if i <= N:
    if not vis[i]:
      vis[i] = True
    else:
      cnt += 1
  else:
    cnt += 1

l, r = 1, N
while l <= r:
  print(l, r, vis)
  if vis[l]:
    l += 1
  else:
    if cnt >= 2:
      cnt -= 2
      vis[l] = True
    else:
      if vis[r]:
        cnt += 1
        vis[r] = False
      r -= 1

print(l-1)