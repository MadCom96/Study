# 적록색약
from collections import deque

n = int(input())
area = [input() for _ in range(n)]
# visited 1 일반시야, 2 색약시야
visited_1 = [[False] * n for _ in range(n)]
visited_2 = [[False] * n for _ in range(n)]
    
dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]

def bfs(y, x, c: set):
    global area, visited_1, visited_2
    visited = []
    if 'B' in c:
        visited = [visited_1, visited_2]
    elif 'R' in c and 'G' in c:
        visited = [visited_2]
    else:
        visited = [visited_1]

    for visited_n in visited:
        visited_n[y][x] = True

    q = deque([(y, x)])
    while q:
        y, x = q.popleft()
        for i in range(4):
            yy = y + dy[i]
            xx = x + dx[i]
            if 0 <= yy < n and 0 <= xx < n:
                # 방문했다면 continue
                v_check = True
                for visited_n in visited:
                    v_check = v_check and visited_n[yy][xx]
                if v_check:
                    continue
                # 방문하지 않았다면 검사 후 방문처리
                if area[yy][xx] in c:
                    q.append((yy, xx))
                    for visited_n in visited:
                        visited_n[yy][xx] = True

cnt_1 = 0
cnt_2 = 0

for y in range(n):
    for x in range(n):
        if not visited_1[y][x] and area[y][x] == 'B':
            # 파란색은 그냥탐색
            bfs(y, x, 'B')
            cnt_1 += 1
            cnt_2 += 1

        else:
            if visited_1[y][x] and visited_2[y][x]:
                continue

            # 그외는 상황별 탐색
            if not visited_2[y][x]:
                # 색약시야로 탐색
                bfs(y, x, set(['R', 'G']))
                cnt_2 += 1

            if not visited_1[y][x]:
                # 일반시야로 탐색
                bfs(y, x, area[y][x])
                cnt_1 += 1

print(cnt_1, cnt_2)