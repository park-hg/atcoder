import sys

sys.stdin = open('input.txt')
N, M = map(int, sys.stdin.readline().split())
A = list(map(int, sys.stdin.readline().split()))
A.sort()
nums = {}
for a in A:
    if a not in nums:
        nums[a] = 1
    else:
        nums[a] += 1

if len(nums) == M:
    print(0)
    exit(0)
k_list = list(nums.keys())
for i, a in enumerate(k_list):
    if (a+1) % M not in nums:
        break

s = {}
for _ in range(len(nums)):
    a = k_list[i]
    if (a+1) % M not in nums:
        s[a] = a*nums[a]
    else:
        s[a] = a*nums[a] + s[(a+1) % M]
    i = (i-1) % len(nums)
print(sum(A)-max(s.values()))
