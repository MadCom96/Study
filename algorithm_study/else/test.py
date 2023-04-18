from heapq import *

tc = int(input())

n = 0
cells = []

# 우하좌상
dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

points = []
dir_s = []

answers = []

def initializedCells():
    global n, cells
    for y in range(n):
        for x in range(n):
            if cells[y][x] == 2:
                cells[y][x] = 0

def simulation():
    global n, cells, dy, dx, points, dir_s, answers

    ans = 0
    cnt = 0
    for i in range(len(points)):
        y, x = points[i]
        d = dir_s[i]
        if d == -1:
            continue
        for j in range(1, 12):
            yy = y + dy[d]*j
            xx = x + dx[d]*j
            if not (0 <= yy < n and 0 <= xx < n):
                ans += abs(yy-y) + abs(xx-x) - 1
                cnt += 1
                break
            if cells[yy][xx] == 0:
                cells[yy][xx] = 2
            else:
                initializedCells()
                return

    heappush(answers, (-cnt, ans))
    initializedCells()
    

def dfs(ith):
    global cells, dy, dx, points, dir_s

    if ith == len(dir_s):
        simulation()
    else:
        for i in range(-1, 4):
            dir_s[ith] = i
            dfs(ith+1)

def prob():
    global n, cells, dy, dx, points, dir_s, answers

    n = int(input())

    for _ in range(n):
        cells.append(list(map(int, input().split())))

    points = []
    for y in range(1, n-1):
        for x in range(1, n-1):
            if cells[y][x] == 1:
                points.append((y, x))

    dir_s = [0] * len(points)
    dfs(0)
    test = heappop(answers)
    return test[1]


for t in range(tc):
    cells = []
    points = []
    dir_s = []
    answers = []
    print(f'#{t+1} {prob()}')