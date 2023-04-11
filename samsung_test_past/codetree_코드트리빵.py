from collections import deque

n, m = map(int, input().split())
# 격자 크기, 사람 수
cells = [list(map(int, input().split())) for _ in range(n)]
# 0 빈 공간, 1 베이스캠프

basecamps = []
basecamps_available = []
cnt = 0
for y in range(n):
    for x in range(n):
        if cells[y][x] == 1:
            basecamps.append((y, x))
            cnt += 1
            basecamps_available.append(cnt)

destination = [(-1, -1)]
people = [[-1, -1]]
people_available = []
for _ in range(m):
    y, x = map(int, input().split())
    destination.append((y-1, x-1))
    people.append([-1, -1])

unpassable = [[False] * n for _ in range(n)]

dy = [-1, 0, 0, 1]
dx = [0, -1, 1, 0]

time = 0

def getDist(sy, sx, ey, ex):
    global n, m, cells, basecamps, basecamps_available, destination, people, people_available, unpassable, dy, dx, time

    if sy == ey and sx == ex:
        return (0, -1)

    bfs = deque()
    visited = [[False] * n for _ in range(n)]

    visited[sy][sx] = True
    for i in range(4):
        yy = sy + dy[i]
        xx = sx + dx[i]
        if not (0 <= yy < n and 0 <= xx < n):
            continue
        if unpassable[yy][xx]:
            continue
        visited[yy][xx] = True
        bfs.append((yy, xx, 1, i))

    while bfs:
        y, x, d, startedDirection = bfs.popleft()
        if y == ey and x == ex:
            return (d, startedDirection)
        for i in range(4):
            yy = y + dy[i]
            xx = x + dx[i]
            if not (0 <= yy < n and 0 <= xx < n):
                continue
            if visited[yy][xx] or unpassable[yy][xx]:
                continue
            visited[yy][xx] = True
            bfs.append((yy, xx, d + 1, startedDirection))
    return (226, 0)

def step1():
    global n, m, cells, basecamps, basecamps_available, destination, people, people_available, unpassable, dy, dx, time
    global n, m, cells, basecamps, destination, people, people_available, unpassable, dy, dx, time
    for pi in people_available:
        sy, sx = people[pi][0], people[pi][1]
        ey, ex = destination[pi]
        _, startedDir = getDist(sy, sx, ey, ex)
        people[pi][0] = sy + dy[startedDir]
        people[pi][1] = sx + dx[startedDir]

def step2():
    global n, m, cells, basecamps, basecamps_available, destination, people, people_available, unpassable, dy, dx, time
    outList = set()
    for pi in people_available:
        sy, sx = people[pi][0], people[pi][1]
        ey, ex = destination[pi]
        if sy == ey and sx == ex:
            outList.add(pi)
            unpassable[ey][ex] = True
    people_available = set(people_available)
    people_available = people_available - outList
    people_available = list(people_available)

def step3():
    global n, m, cells, basecamps, basecamps_available, destination, people, people_available, unpassable, dy, dx, time
    if time <= m:
        shortestL = 226
        shortestI = -1
        for bi in range(len(basecamps)):
            # basecamps[bi] 와 도착지점과의 거리를 구한다.
            sy, sx = basecamps[bi]
            ey, ex = destination[time]
            # print(sy, sx, ey, ex)
            # print(*unpassable, sep='\n')
            d, _ = getDist(sy, sx, ey, ex)
            if d < shortestL:
                shortestL = d
                shortestI = bi
        
        # basecamps[shortestI] 위치 에 사람 추가
        y, x = basecamps.pop(shortestI)

        people[time] = [y, x]
        people_available.append(time)
        unpassable[y][x] = True

while True:
    time += 1
    input()
    step1()
    print("이동 후")
    print(people)
    print(destination)
    step2()
    print("도착 한 사람 제거")
    print(*unpassable, sep='\n')
    step3()
    print("새사람 추가")
    print(people)
    print(destination)
    print(*unpassable, sep='\n')
    if len(people_available) == 0:
        print(time)
        break