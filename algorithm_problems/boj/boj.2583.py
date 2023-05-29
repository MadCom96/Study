# 영역 구하기
from collections import deque
m, n, k = map(int, input().split())

cells = [[True] * n for _ in range(m)]

for i in range(k):
    # y1, x1, y2, x2 = map(int, input().split())
    x1, y1, x2, y2 = map(int, input().split())
    for y in range(y1, y2):
        for x in range(x1, x2):
            cells[y][x] = False

def bfs(y, x):
    global m, n, cells
    dy = [0, 0, 1, -1]
    dx = [1, -1, 0, 0]

    cnt = 0
    cells[y][x] = False
    dq = deque([(y, x)])
    while dq:
        y, x = dq.popleft()
        cnt += 1
        for i in range(4):
            yy = y + dy[i]
            xx = x + dx[i]
            if 0<=yy<m and 0<=xx<n and cells[yy][xx]:
                cells[yy][xx] = False
                dq.append((yy,xx))
    return cnt

ans = 0
areas = []
for y in range(m):
    for x in range(n):
        # print()
        # print(*cells, sep='\n')
        if cells[y][x]:
            areas.append(bfs(y, x))
            ans += 1
areas.sort()

print(ans)
print(*areas)