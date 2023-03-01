# 귀경길 교통상황을 알려드립니다
import sys
from collections import deque
input = sys.stdin.readline

n = int(input().rstrip())
g = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    a, b = map(int, input().rstrip().split())
    g[a].append(b)
    g[b].append(a)

cars = list(map(int, input().rstrip().split()))
count_car = cars.count(1)
cars.insert(0, 0)

time = 0
bfs = deque()
visited = [False] * (n + 1)
visited[1] = True

# bfs마다
while True:
    bfs = deque()
    bfs.append(1)
    time += 1
    visited = [False] * (n + 1)
    visited[1] = True
    # 시간마다
    while len(bfs) != 0:
        now = bfs.popleft()
        if now == 1 and cars[now] == 1:
            cars[now] = 0
            count_car -= 1
            if count_car == 0:
                print(time)
                exit(0)
        for conn in g[now]:
            if not visited[conn]:
                visited[conn] = True
                bfs.append(conn)
                if cars[now] == 0 and cars[conn] == 1:
                    cars[now] = 1
                    cars[conn] = 0