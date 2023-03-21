# 냉방 시스템
from collections import deque
from copy import deepcopy

n, m, k = map(int, input().split())

office = [list(map(int, input().split())) for _ in range(n)]
acEffect = [[0] * n for _ in range(n)]
officeArea = []

isWall = []
for y1 in range(n):
    a = []
    for x1 in range(n):
        b = []
        for y2 in range(n):
            c = []
            for x2 in range(n):
                c.append(False)
            b.append(c)
        a.append(b)
    isWall.append(a)

for _ in range(m):
    y1, x1, direction = map(int, input().split())
    y1 -= 1
    x1 -= 1
    y2, x2 = y1, x1
    # 벽이 외벽에 포함되게 주어지는 경우 역시 없다고 가정해도 좋습니다.
    if direction == 0:
        y2 -= 1
    else:
        x2 -= 1
    isWall[y1][x1][y2][x2] = True
    isWall[y2][x2][y1][x1] = True

d = deque()
reachable = [] 
for y in range(n):
    for x in range(n):
        if office[y][x] == 0:
            continue
        elif office[y][x] == 1:
            officeArea.append((y, x))

        # 왼쪽
        elif office[y][x] == 2:
            d.append((y, x-1, 5))
            reachable = [[False] * n for _ in range(n)]
            reachable[y][x-1] = True
            while d:
                yy, xx, nn = d.popleft()
                acEffect[yy][xx] += nn
                if nn == 1:
                    continue
                if xx - 1 < 0:
                    continue
                if yy - 1 >= 0 and (not reachable[yy-1][xx-1]) and \
                    (not isWall[yy][xx][yy-1][xx]) and (not isWall[yy-1][xx][yy-1][xx-1]):
                    reachable[yy-1][xx-1] = True
                    d.append((yy-1, xx-1, nn-1))
                if not reachable[yy][xx-1] and \
                    (not isWall[yy][xx][yy][xx-1]):
                    reachable[yy][xx-1] = True
                    d.append((yy, xx-1, nn-1))
                if yy + 1 < n and (not reachable[yy+1][xx-1]) and \
                    (not isWall[yy][xx][yy+1][xx]) and (not isWall[yy+1][xx][yy+1][xx-1]):
                    reachable[yy+1][xx-1] = True
                    d.append((yy+1, xx-1, nn-1))
       # 위쪽
        elif office[y][x] == 3:
            d.append((y-1, x, 5))
            reachable = [[False] * n for _ in range(n)]
            reachable[y-1][x] = True
            while d:
                yy, xx, nn = d.popleft()
                acEffect[yy][xx] += nn
                if nn == 1:
                    continue
                if yy - 1 < 0:
                    continue
                if xx - 1 >= 0 and (not reachable[yy-1][xx-1]) and \
                    (not isWall[yy][xx][yy][xx-1]) and (not isWall[yy][xx-1][yy-1][xx-1]):
                    reachable[yy-1][xx-1] = True
                    d.append((yy-1, xx-1, nn-1))
                if not reachable[yy-1][xx] and \
                    (not isWall[yy][xx][yy-1][xx]):
                    reachable[yy-1][xx] = True
                    d.append((yy-1, xx, nn-1))
                if xx + 1 < n and (not reachable[yy-1][xx+1]) and \
                    (not isWall[yy][xx][yy][xx+1]) and (not isWall[yy][xx+1][yy-1][xx+1]):
                    reachable[yy-1][xx+1] = True
                    d.append((yy-1, xx+1, nn-1))
        # 오른쪽
        elif office[y][x] == 4:
            d.append((y, x+1, 5))
            reachable = [[False] * n for _ in range(n)]
            reachable[y][x+1] = True
            while d:
                yy, xx, nn = d.popleft()
                acEffect[yy][xx] += nn
                if nn == 1:
                    continue
                if xx + 1 >= n:
                    continue
                if yy - 1 >= 0 and (not reachable[yy-1][xx+1]) and \
                    (not isWall[yy][xx][yy-1][xx]) and (not isWall[yy-1][xx][yy-1][xx+1]):
                    reachable[yy-1][xx+1] = True
                    d.append((yy-1, xx+1, nn-1))
                if not reachable[yy][xx+1] and \
                    (not isWall[yy][xx][yy][xx+1]):
                    reachable[yy][xx+1] = True
                    d.append((yy, xx+1, nn-1))
                if yy + 1 < n and (not reachable[yy+1][xx+1]) and \
                    (not isWall[yy][xx][yy+1][xx]) and (not isWall[yy+1][xx][yy+1][xx+1]):
                    reachable[yy+1][xx+1] = True
                    d.append((yy+1, xx+1, nn-1))
        # 아래쪽
        elif office[y][x] == 5:
            d.append((y+1, x, 5))
            reachable = [[False] * n for _ in range(n)]
            reachable[y+1][x] = True
            while d:
                yy, xx, nn = d.popleft()
                acEffect[yy][xx] += nn
                if nn == 1:
                    continue
                if yy + 1 >= n:
                    continue
                if xx - 1 >= 0 and (not reachable[yy+1][xx-1]) and \
                    (not isWall[yy][xx][yy][xx-1]) and (not isWall[yy][xx-1][yy+1][xx-1]):
                    reachable[yy+1][xx-1] = True
                    d.append((yy+1, xx-1, nn-1))
                if not reachable[yy+1][xx] and \
                    (not isWall[yy][xx][yy+1][xx]):
                    reachable[yy+1][xx] = True
                    d.append((yy+1, xx, nn-1))
                if xx + 1 < n and (not reachable[yy+1][xx+1]) and \
                    (not isWall[yy][xx][yy][xx+1]) and (not isWall[yy][xx+1][yy+1][xx+1]):
                    reachable[yy+1][xx+1] = True
                    d.append((yy+1, xx+1, nn-1))

office = [[0] * n for _ in range(n)]
for t in range(101):
    done = True
    for officeA in officeArea:
        y, x = officeA
        if office[y][x] >= k:
            pass
        else:
            done = False
            break
    if done:
        print(t)
        exit()

    # step 1.
    for y in range(n):
        for x in range(n):
            office[y][x] += acEffect[y][x]
    # step 2.
    office_next = deepcopy(office)
    dy = [0, 0, 1, -1]
    dx = [1, -1, 0, 0]
    for y in range(n):
        for x in range(n):
            for i in range(4):
                yy = y + dy[i]
                xx = x + dx[i]
                if 0 <= yy < n and 0 <= xx < n:
                    if isWall[y][x][yy][xx]:
                        continue
                    diff = max(0, office[y][x] - office[yy][xx])
                    diff //= 4
                    office_next[y][x] -= diff
                    office_next[yy][xx] += diff 
    office = office_next
    # step 3.
    for x in range(n):
        office[0][x] = max(office[0][x] - 1, 0)
        office[-1][x] = max(office[-1][x] - 1, 0)
    for y in range(1, n-1):
        office[y][0] = max(office[y][0] - 1, 0)
        office[y][-1] = max(office[y][-1] - 1, 0)

print(-1)