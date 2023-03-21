# 팩맨
from copy import deepcopy

m, t = map(int, input().split())
r, c = map(int, input().split())

monsters = []
for i in range(5):
    l = []
    for j in range(5):
        l.append([])
    monsters.append(l)

for _ in range(m):
    y, x, d = map(int, input().split())
    monsters[y][x].append(d)
# r, c, d
# 방향 d는 1부터 순서대로 ↑, ↖, ←, ↙, ↓, ↘, →, ↗ 를 의미합니다.
# 턴이 진행되는 동안 살아있는 몬스터의 수가 100만개가 넘는 입력은 주어지지 않는다고 가정해도 좋습니다.

eggs = []
dead_monsters = []
for i in range(5):
    l = []
    for j in range(5):
        l.append([])
    dead_monsters.append(l)

dy = [0, -1, -1, 0, 1, 1, 1, 0, -1]
dx = [0, 0, -1, -1, -1, 0, 1, 1, 1]

def monster_duplication_attempt():
    global monsters, eggs
    eggs = deepcopy(monsters)

def monster_moveable(y, x, d):
    global  r, c, dy, dx
    yy = y + dy[d]
    xx = x + dx[d]
    # 격자 밖으로는 움직일 수 없다.
    if not (0 < yy <= 4 and 0 < xx <= 4):
        return False
    # 팩맨 있는 경우
    if yy == r and xx == c:
        return False
    # 죽은 몬스터 있는 경우
    if dead_monsters[yy][xx]:
        return False
    return True

def monster_move():
    global monsters, dy, dx
    monsters_next = []
    for i in range(5):
        l = []
        for j in range(5):
            l.append([])
        monsters_next.append(l)
    for y in range(1, 5):
        for x in range(1, 5):
            for di in range(len(monsters[y][x])):
                d = monsters[y][x][di]
                counter8 = 8
                while (not monster_moveable(y, x, d)) and (counter8 != 0):
                    counter8 -= 1
                    d -= 1
                    d = (d + 1) % 8
                    d += 1
                if counter8 == 0:
                    monsters_next[y + dy[0]][x + dx[0]].append(d)
                else:
                    monsters_next[y + dy[d]][x + dx[d]].append(d)

    # 수정 가능성
    monsters = monsters_next

most = -1
most_order = []
def dfs(r, c, total, move_order):
    global most, most_order, dy, dx, monsters

    if len(move_order) == 3:
        if total > most:
            most = total
            most_order = move_order[:]
        return
    
    for i in (1, 3, 5, 7):
        rr = r + dy[i]
        cc = c + dx[i]
        if 0 < rr <= 4 and 0 < cc <= 4:
            # 옮기는 과정 수정 가능성
            tmp = monsters[rr][cc]
            monsters[rr][cc] = []
            total += len(tmp)

            dfs(rr, cc, total, move_order + [i])

            monsters[rr][cc] = tmp
            total -= len(tmp)


def packman_move():
    global r, c, dy, dx, most, most_order, monsters, dead_monsters
    # 1, 3, 5, 7 순서
    most = -1
    most_order = []
    dfs(r, c, 0, [])
    for move in most_order:
        r += dy[move]
        c += dx[move]
        dead_monsters[r][c].extend([0]*len(monsters[r][c]))
        monsters[r][c] = []

def dead_turn_count():
    global dead_monsters
    for y in range(1, 5):
        for x in range(1, 5):
            for i in range(len(dead_monsters[y][x])):
                dead_monsters[y][x][i] += 1

def monster_body_clear():
    global dead_monsters
    for y in range(1, 5):
        for x in range(1, 5):
            i = 0
            while i < len(dead_monsters[y][x]):
                if dead_monsters[y][x][i] == 2:
                    dead_monsters[y][x].pop(i)
                else:
                    i += 1

def monster_duplication_complete():
    for y in range(1, 5):
        for x in range(1, 5):
            monsters[y][x].extend(eggs[y][x])

def turn():
    dead_turn_count()
    monster_duplication_attempt()
    monster_move()
    packman_move()
    monster_body_clear()
    monster_duplication_complete()


for ti in range(t):
    turn()

ans = 0
for y in range(1, 5):
    for x in range(1, 5):
        ans += len(monsters[y][x])
print(ans)