import math
a, b, c, d = map(int, input().split())

if c*d-b == 0:
    if a <= 0:
        print(0)
    else:
        print(-1)
elif c*d-b > 0:
    print(int(math.ceil(a/(c*d-b))))
else:
    print(-1)