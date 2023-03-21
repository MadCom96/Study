# 시공의 돌풍
from copy import deepcopy
n, m, t = map(int, input().split())
cells = [list(map(int, input().split())) for _ in range(n)]
cells_next = []

dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]

def diffusion():
    global n, m, t, cells, cells_next, dy, dx
    cells_next = deepcopy(cells)
    for y in range(n):
        for x in range(m):
            if cells[y][x] == -1:
                continue
            diffuse_amount = cells[y][x] // 5
            for i in range(4):
                yy = dy[i] + y
                xx = dx[i] + x
                if 0 <= yy < n and 0 <= xx < m and cells[yy][xx] != -1:
                    cells_next[yy][xx] += diffuse_amount
                    cells_next[y][x] -= diffuse_amount
    cells = deepcopy(cells_next)


def cleaning():
    global n, m, t, cells, cells_next, dy, dx
    start = []
    for i in range(n):
        if cells[i][0] == -1:
            start.append(i)
            start.append(i+1)
            break
    dir = [3, 0, 2, 1]
    start_loc = [start[0], 0]
    while True:
        yy = start_loc[0] + dy[dir[0]]
        xx = start_loc[1] + dx[dir[0]]
        if dir[0] == 3:
            if yy == -1:
                dir.pop(0)
                continue
        elif dir[0] == 0:
            if xx == m:
                dir.pop(0)
                continue
        elif dir[0] == 2:
            if yy == start[0] + 1:
                dir.pop(0)
                continue
        elif dir[0] == 1:
            if xx == 0:
                cells[start_loc[0]][start_loc[1]] = 0
                dir.pop(0)
                break
        cells[start_loc[0]][start_loc[1]] = cells[yy][xx]
        start_loc[0] = yy
        start_loc[1] = xx
    
    dir = [2, 0, 3, 1]
    start_loc = [start[1], 0]
    while True:
        yy = start_loc[0] + dy[dir[0]]
        xx = start_loc[1] + dx[dir[0]]
        if dir[0] == 2:
            if yy == n:
                dir.pop(0)
                continue
        elif dir[0] == 0:
            if xx == m:
                dir.pop(0)
                continue
        elif dir[0] == 3:
            if yy == start[1] - 1:
                dir.pop(0)
                continue
        elif dir[0] == 1:
            if xx == 0:
                cells[start_loc[0]][start_loc[1]] = 0
                dir.pop(0)
                break
        cells[start_loc[0]][start_loc[1]] = cells[yy][xx]
        start_loc[0] = yy
        start_loc[1] = xx
    cells[start[0]][0] = -1
    cells[start[1]][0] = -1
    


def total():
    global n, m, t, cells, cells_next, dy, dx
    ans = 0
    for i in range(n):
        ans += sum(cells[i])
    ans += 2
    print(*cells, sep='\n')
    print()
    return ans
        

for _ in range(t):
    diffusion()
    cleaning()
print(total())