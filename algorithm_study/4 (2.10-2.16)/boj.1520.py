# 내리막 길
import sys
from collections import deque
# 10000으로 줄이고 메모리초과 해결
sys.setrecursionlimit(10001)

m, n = map(int, input().split())
heights = [list(map(int, input().split())) for _ in range(m)]
# -1로 설정하고 시간초과 해결
dp = [[-1] * n for _ in range(m)]
dp[m-1][n-1] = 1

dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]

def dfs(y, x):
    global dp, heights, m, n, dy, dx
    if dp[y][x] != -1:
        return dp[y][x]
    now = 0
    for i in range(4):
        if 0 <= y + dy[i] < m and 0 <= x + dx[i] < n:
            if heights[y+dy[i]][x+dx[i]] < heights[y][x]:
                now += dfs(y + dy[i], x + dx[i])
    dp[y][x] = now
    return now

print(dfs(0, 0))

# 깊이 허용범위를 10000으로 줄이니 해결됐다... why?