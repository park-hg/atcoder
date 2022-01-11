n = int(input())
t = list(map(int, input().split()))
m = sum(t)
dp = [False] * (m+1)
dp[t[0]] = True

for i in range(n):
    for j in range(m+1):
        if dp[j] and j+t[i] <= m:
            dp[j+t[i]] = True

ans = float('inf')
for i in range(m+1):
    if dp[i] and ans > max(i, m-i):
        ans = max(i, m-i)

print(ans)