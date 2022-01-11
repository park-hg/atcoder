import sys

sys.stdin = open('input.txt', 'r')
town = []
for i in range(4):
    l = list(map(int, sys.stdin.readline().split()))
    for j in range(4):
        if l[j] == 1:
            town.append((i+1, j+1))

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
def dfs(s, grid, num):
    cnt = 0
    visited = [[False]*6 for _ in range(6)]
    stack = [s]
    while stack:
        x, y = stack.pop()
        if not visited[x][y]:
            visited[x][y] = True
            cnt += 1
            for i in range(4):
                nx, ny = x+dx[i], y+dy[i]
                if 0 <= nx < 6 and 0 <= ny < 6 and grid[nx][ny] == num:
                    stack.append((nx, ny))
    return cnt

def check(bit):
    grid = [[0]*6 for _ in range(6)]
    cnt = 0
    for i in range(16):
        if bit & (1 << i):
            k, j = i//4, i%4
            grid[k+1][j+1] = 1
            cnt += 1
    for i, j in town:
        if grid[i][j] != 1:
            return False
    breaker = False
    for i in range(4):
        for j in range(4):
            if grid[i][j] == 1:
                breaker = True
                break
        if breaker:
            break
    inner = dfs((i, j), grid, 1)
    if inner != cnt:
        return False
    outer = dfs((0, 0), grid, 0)
    if inner + outer != 6*6:
        return False          
    return True

ans = 0
for bit in range(1 << 16):
    if check(bit):
        ans += 1
print(ans)