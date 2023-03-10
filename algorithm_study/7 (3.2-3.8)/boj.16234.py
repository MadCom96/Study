# 인구 이동
from collections import deque
n, l, r = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(n)]
# 0 방문한적 없음, 1 이번에 한 연합, 2 연합체크 완료
visited = []
dq = []

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(y, x) -> int:
    global n, l, r, A, visited, dq
    visited[y][x] = 1
    dq = deque([(y, x)])
    sum = 0
    cells = 0
    while dq:
        yy, xx = dq.popleft()
        sum += A[yy][xx]
        cells += 1
        for i in range(4):
            yyy = yy + dy[i]
            xxx = xx + dx[i]
            if 0 <= yyy < n and 0 <= xxx < n:
                if l <= abs(A[yy][xx] - A[yyy][xxx]) <= r:
                    if visited[yyy][xxx] == 0:
                        visited[yyy][xxx] = 1
                        dq.append((yyy, xxx))
    return sum // cells

def move(y, x, avg):
    global n, l, r, A, visited, dq
    dq = deque([(y, x)])
    cells = 0
    visited[y][x] = 2
    while dq:
        yy, xx = dq.popleft()
        cells += 1
        A[yy][xx] = avg
        for i in range(4):
            yyy = yy + dy[i]
            xxx = xx + dx[i]
            if 0 <= yyy < n and 0 <= xxx < n:
                if visited[yyy][xxx] == 1:
                    visited[yyy][xxx] = 2
                    dq.append((yyy, xxx))
    return cells > 1

def check(y, x) -> bool:
    global visited
    # 방문체크
    if visited[y][x] == 2:
        return False
    # bfs
    avg = bfs(y, x)
    # 이동
    return move(y, x, avg)

day = 0
# 하나의 while loop는 하루를 뜻한다.
while True:
    visited = [[0] * n for _ in range(n)]
    everMoved = False
    print(f'day{day}')
    for y in range(n):
        for x in range(n):
            c = check(y, x)
            everMoved = everMoved or c
            if c:
                print(*A, sep='\n')
                print()

    if not everMoved:
        break
    day += 1

print(day)