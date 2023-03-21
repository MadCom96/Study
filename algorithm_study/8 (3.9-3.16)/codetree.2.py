# 생명과학부 랩 인턴
from copy import deepcopy

n, m, k = map(int, input().split())

cells = [[0] * m for _ in range(n)]
molds = []
molds_next = []

dy = [0, -1, 1, 0, 0]
dx = [0, 0, 0, 1, -1]

for i in range(k):
    y, x, s, d, b = map(int, input().split())
    cells[y-1][x-1] = b
    molds.append((y-1, x-1, s, d, b))

ans = 0
for xi in range(m):
    flag = False
    for yi in range(n):
        if cells[yi][xi] != 0:
            for mi in range(len(molds)):
                if molds[mi][4] == cells[yi][xi]:
                    ans += cells[yi][xi]
                    molds.pop(mi)
                    cells[yi][xi] = 0
                    flag = True
                    break
        if flag:
            break
    
    molds_next = []
    cells_next = [[0] * m for _ in range(n)]
    for mi in range(len(molds)):
        y, x, s, d, b = molds[mi]
        if cells[y][x] != b:
            continue
        yy = y + s * dy[d]
        xx = x + s * dx[d]
        if d == 1:
            yy %= 2 * (n - 1)
            if yy >= n:
                d = 2
                yy = n - 1 - (yy - (n - 1))
        elif d == 2:
            yy %= 2 * (n - 1)
            if yy >= n:
                d = 1
                yy = n - 1 - (yy - (n - 1))
        elif d == 3:
            xx %= 2 * (m - 1)
            if xx >= m:
                d = 4
                xx = m - 1 - (xx - (m - 1))
        elif d == 4:
            xx %= 2 * (m - 1)
            if xx >= m:
                d = 3
                xx = m - 1 - (xx - (m - 1))
        
        # from (y, x) to (yy, xx)
        if cells_next[yy][xx] < b:
            cells_next[yy][xx] = b
            molds_next.append((yy, xx, s, d, b))
    cells = cells_next
    molds = molds_next

print(ans)