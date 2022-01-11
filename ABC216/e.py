import sys

sys.stdin = open('input.txt', 'r')

n, k = map(int, sys.stdin.readline().split())
a = list(map(int, sys.stdin.readline().split()))

a.sort(reverse=True)
a.append(0)

def summation(start, end):
    return (start+end)*(start-end+1)//2

s = 0
for i in range(0, len(a)-1):
    s += (i+1)*(a[i]-a[i+1])
    if s > k:
        s -= (i+1)*(a[i]-a[i+1])
        break
ans = 0
if s == sum(a):
    for j in range(len(a)-1):
        ans += summation(a[j], 1)
else:
    for idx in range(i):
        ans += summation(a[0], a[i]+1)
    ans += (i+1)*summation(a[i], a[i]-(k-s)//(i+1)+1)
    ans += ((k-s)%(i+1))*(a[i]-(k-s)//(i+1))

print(ans)