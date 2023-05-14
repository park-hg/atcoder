import sys
sys.stdin = open('input.txt')
N, M = map(int, sys.stdin.readline().split())
A = list(map(int, sys.stdin.readline().split()))
A.sort()
if N == 1:
    print(0)
    exit()

idx_A = {}
for i, a in enumerate(A):
    if a not in idx_A:
        idx_A[a] = [a]
    else:
        idx_A[a].append(a)

keys = list(idx_A.keys())
group_idx = [-1]*len(keys)

for i in range(len(keys)):
    if (keys[(i+1) % len(keys)] - keys[i]) % M != 1:
        break

s = (i+1) % len(keys)
cur = keys[s]
while group_idx[s] == -1:
    group_idx[s] = cur
    new_s = (s+1) % len(keys)
    if (keys[new_s] - keys[s]) % M != 1:
        cur = keys[new_s]
    s = new_s

nums_dict = {}
for idx, k in zip(group_idx, keys):
    if idx in nums_dict:
        nums_dict[idx] += idx_A[k]
    else:
        nums_dict[idx] = idx_A[k]

ans = 10**100
tmp = sum(A)
for k in nums_dict:
    ans = min(ans, tmp-sum(nums_dict[k]))
print(ans)
