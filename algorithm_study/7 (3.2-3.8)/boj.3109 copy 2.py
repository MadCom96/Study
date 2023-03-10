# 빵집
import sys
input = sys.stdin.readline

r, c = map(int, input().split())
lines = [list(input().rstrip()) for _ in range(r)]

dy = [-1, 0, 1]

def dfs(y, x):
    global r, c, lines
    lines[y][x] = 'x'
    if x == c - 1:
        return True
    to = 0
    for d in dy:
        if 0 <= d + y < r and lines[d+y][x+1] != 'x':
            to += 1
            if dfs(d + y, x + 1):
                return True
    if to == 0:
        return False

ans = 0
for i in range(r):
    if dfs(i, 0):
        ans += 1
print(ans)