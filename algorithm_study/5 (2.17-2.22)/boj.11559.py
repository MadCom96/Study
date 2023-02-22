# Puyo Puyo
from collections import deque
import copy as c

q = deque()
color = '.'
puyo = [list(input()) for _ in range(12)]
visited = []
visited_tmp = []

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

# 현재 화면에서 가능한 연쇄를 계산
# 몇 그룹을 없앴는지 숫자로 반환
def bfs() -> int:
    global q, color, puyo, visited, visited_tmp, dx, dy
    count = 1
    copy = q[0]
    while q:
        y, x = q.popleft()
        for i in range(4):
            if 0 <= y+dy[i] <= 11 and 0 <= x+dx[i] <= 5:
                if visited_tmp[y+dy[i]][x+dx[i]]:
                    continue
                if puyo[y+dy[i]][x+dx[i]] == color:
                    q.append((y+dy[i], x+dx[i]))
                    visited_tmp[y+dy[i]][x+dx[i]] = True
                    count += 1
    if count >= 4:
        q.append(copy)
        while q:
            y,  x = q.popleft()
            puyo[y][x] = '.'
            for i in range(4):
                if 0 <= y+dy[i] <= 11 and 0 <= x+dx[i] <= 5:
                    if visited[y+dy[i]][x+dx[i]]:
                        continue
                    if puyo[y+dy[i]][x+dx[i]] == color:
                        q.append((y+dy[i], x+dx[i]))
                        visited[y+dy[i]][x+dx[i]] = True
        return True
    else:
        visited = c.deepcopy(visited_tmp)
        return False

# 연쇄 계산 후 없어진 칸을 모두 내린다.
def renew():
    global q, color, puyo, visited, visited_tmp, dx, dy
    for i in range(0, 6):
        tmp = []
        for j in range(11, -1, -1):
            if puyo[j][i] != '.':
                tmp.append(puyo[j][i])
                puyo[j][i] = '.'
        j = 11
        while tmp:
            puyo[j][i] = tmp.pop(0)
            j -= 1


ans = 0
while True:
    visited = [[False] * 6 for _ in range(12)]
    removed_group = 0
    for i in range(12):
        for j in range(6):
            if puyo[i][j] != '.' and visited[i][j] == False:
                visited[i][j] = True
                visited_tmp = c.deepcopy(visited)
                color = puyo[i][j]
                q.append((i, j))
                isRemovable = bfs()
                if isRemovable:
                    removed_group += 1
    # 연쇄가 없다면 출력 후 프로그램 끝
    if removed_group == 0:
        print(ans)
        exit(0)
    # 연쇄가 있다면 빈공간을 채워줘야 된다.
    else:
        ans += 1
        renew()