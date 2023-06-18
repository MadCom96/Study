#아기상어
from collections import deque

n = int(input())
field = []
babyshark = ()
weight = 2
ate = 0

y, x = -1, -1
for _ in range(n):
    y += 1
    line = list(map(int, input().split()))
    field.append(line)
    for x in range(n):
        if line[x] == 9:
            babyshark = (y, x)

dy = [-1, 0, 0, 1]
dx = [0, -1, 1, 0]
def bfs(y, x) -> tuple:
    global n, field, weight
    dq = deque([(y, x, 1)])
    visited = [[False] * n for _ in range(n)]
    visited[y][x] = True
    shortestLen = 10000
    can = ()
    while dq:
        y, x, length = dq.popleft()
        if shortestLen < length:
            return can
        for i in range(4):
            yy = y + dy[i]
            xx = x + dx[i]
            if not (0<= yy <n and 0<= xx <n) or visited[yy][xx]:
                continue
            if field[yy][xx] != 0 and field[yy][xx] < weight:
                shortestLen = length
                if can != ():
                    if can[0] > yy:
                        can = (yy, xx, length)
                    elif can[0] == yy and can[1] > xx:
                        can = (yy, xx, length)
                else:
                    can = (yy, xx, length)
            if field[yy][xx] <= weight:
                dq.append((yy, xx, length + 1))
            visited[yy][xx] = True
        
    return (-1, -1, -1)


ans = 0
while True:
    # 수정가능
    y, x = babyshark
    # 다음 행선지를 반환
    yy, xx, length = bfs(*babyshark)
    if yy == -1:
        break
    field[yy][xx] = 9
    field[y][x] = 0
    babyshark = (yy, xx)
    ate += 1
    if ate == weight:
        # ate 초기화?
        ate = 0
        weight += 1
    ans += length

print(ans)