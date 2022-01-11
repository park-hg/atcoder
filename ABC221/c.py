import sys
sys.stdin = open('input.txt', 'r')

N = list(map(int, sys.stdin.readline().rstrip()))

ans = 0
for bit in range(1<<len(N)):
    a = [N[idx] for idx, one in enumerate(bin(bit)[2:]) if one=='1']
    b = [N[idx] for idx, zero in enumerate(bin(bit)[2:]) if zero=='0']
    if len(a) + len(b) == len(N) and len(a) > 0 and len(b) > 0:
        a.sort(reverse=True)
        b.sort(reverse=True)
        a = [str(i) for i in a]
        b = [str(i) for i in b]
        n = ''.join(a)
        m = ''.join(b)
        n = int(n)
        m = int(m)
        ans = max(ans, n*m)

print(ans)