import sys
sys.stdin = open('input.txt')
N, K = map(int, sys.stdin.readline().split())
A = list(map(int, sys.stdin.readline().split()))

left, right = 0, max(A)
while left < right:
  mid = (left+right)//2
  if sum([min(mid, a) for a in A]) < K:
    left = mid + 1
  else:
    right = mid

A_after = [max(a-right+1, 0) for a in A]
answer = []
for a in A:
  if a > right-1:
    answer.append(a-right+1)
    K -= (right-1)
  else:
    answer.append(0)
    K -= a

for i in range(len(answer)):
  if answer[i] == 0:
    continue
  if K > 0:
    answer[i] -= 1
    K -= 1
  if K == 0:
    break

print(*answer)

