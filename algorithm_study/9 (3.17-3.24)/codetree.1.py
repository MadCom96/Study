# 정육면체 한번 더 굴리기
from collections import deque

n, m = map(int, input().split())
cells = [list(map(int, input().split())) for _ in range(n)]
sum_cell = [[0] * n for _ in range(n)]
visited = [[False] * n for _ in range(n)]
updated = [[False] * n for _ in range(n)]

d = deque()
dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]
for y in range(n):
    for x in range(n):
        if visited[y][x]:
            continue
        d.append((y, x))
        total = 0
        visited[y][x] = True
        while d:
            yy, xx = d.popleft()
            total += cells[yy][xx]
            for i in range(4):
                yyy = yy + dy[i]
                xxx = xx + dx[i]
                if not (0 <= yyy < n and 0 <= xxx < n):
                    continue
                if (not visited[yyy][xxx]) and cells[y][x] == cells[yyy][xxx]:
                    visited[yyy][xxx] = True
                    d.append((yyy, xxx))
        
        d.append((y, x))
        updated[y][x] = True
        while d:
            yy, xx = d.popleft()
            sum_cell[yy][xx] = total
            for i in range(4):
                yyy = yy + dy[i]
                xxx = xx + dx[i]
                if not (0 <= yyy < n and 0 <= xxx < n):
                    continue
                if visited[yyy][xxx] and (not updated[yyy][xxx]):
                    updated[yyy][xxx] = True
                    d.append((yyy, xxx))
del visited
del updated

#       0
#   1   2(위) 3   4(아래)   
#       5
dice = [5, 4, 1, 3, 6, 2]
def roll(direction):
    global dice
    # 오른쪽
    if direction == 0:
        dice[1], dice[2], dice[3], dice[4] = dice[4], dice[1], dice[2], dice[3]
    # 아래쪽
    elif direction == 1:
        dice[0], dice[2], dice[5], dice[4] = dice[4], dice[0], dice[2], dice[5]
    # 왼쪽
    elif direction == 2:
        dice[1], dice[2], dice[3], dice[4] = dice[2], dice[3], dice[4], dice[1]
    # 위쪽
    elif direction == 3:
        dice[0], dice[2], dice[5], dice[4] = dice[2], dice[5], dice[4], dice[0]

def get_dice_bottom() -> int:
    global dice
    return dice[4]

ans = 0
direction = 0
y = 0
x = 0
for _ in range(m):
    if not (0 <= y + dy[direction] < n and 0 <= x + dx[direction] < n):
        direction = (direction + 2) % 4
    y += dy[direction]
    x += dx[direction]
    roll(direction)
    ans += sum_cell[y][x]
    if get_dice_bottom() > cells[y][x]:
        direction += 1
        direction %= 4
    elif get_dice_bottom() == cells[y][x]:
        pass
    else:
        direction -= 1
        direction %= 4
print(ans)