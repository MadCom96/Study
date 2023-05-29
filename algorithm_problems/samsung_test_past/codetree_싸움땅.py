n, m, k = map(int, input().split())
# 격자의 크기, 플레이어 수, 라운드 수
# 2 ~ 20, 1 ~ 칸수or30, 1 ~ 500

guns = [list(map(int, input().split())) for _ in range(n)]
# 0은 빈칸, 0 이상은 총의 공격력 ~100,000
players = [list(map(int, input().split())) for _ in range(m)]
# x, y, d, s
# x, y 위치, d 방향, s 초기 능력치 1~100
# 위치는 겹쳐져 주어지지 않고, 초기 위치에는 총이 없다.
players_cells = []
players_gun = [0] * m
players_point = [0] * m

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

def init():
    global n, m, guns, players, players_cells
    players_cells = [[-1] * n for _ in range(n)]
    for pi in range(m):
        players[pi][0] -= 1
        players[pi][1] -= 1
        players_cells[players[pi][0]][players[pi][1]] = pi
    
    for y in range(n):
        for x in range(n):
            if guns[y][x] == 0:
                guns[y][x] = []
            else:
                guns[y][x] = [guns[y][x]]

# attack point
def ap(pi):
    global players, players_gun
    return players[pi][3] + players_gun[pi]

# pi 승 = True, pii 승 = False, 숫자가 포인트
def fight(pi, pii):
    global players
    pip = ap(pi)
    piip = ap(pii)
    if pip > piip:
        return (True, pip - piip)
    elif pip < piip:
        return (False, piip - pip)
    else:
        return (players[pi][3] > players[pii][3], 0)


def players_move():
    global n, m, k, guns, players, players_gun, dy, dx
    for pi in range(m):
        y, x, d, s = players[pi]
        # 1-1
        yy = y + dy[d]
        xx = x + dx[d]
        if not(0 <= yy < n and 0 <= xx < n):
            d = (d + 2) % 4
            players[pi][2] = d
            yy = y + dy[d]
            xx = x + dx[d]
        players_cells[y][x] = -1
        
        # 2-1
        if players_cells[yy][xx] == -1:
            players_cells[yy][xx] = pi
            players[pi][0] = yy
            players[pi][1] = xx

            if players_gun[pi] != 0:
                guns[yy][xx].append(players_gun[pi])
                players_gun[pi] = 0
            
            most_powerful_gun = -1
            power = 0
            for gi in range(len(guns[yy][xx])):
                if power < guns[yy][xx][gi]:
                    power = guns[yy][xx][gi]
                    most_powerful_gun = gi
            
            if most_powerful_gun == -1:
                players_gun[pi] = 0
            else:
                players_gun[pi] = guns[yy][xx].pop(most_powerful_gun)

        # 2-2-1
        else:
            pii = players_cells[yy][xx]
            piWin, point = fight(pi, pii)
            winner = 0
            loser = 0
            if piWin:
                winner = pi
                loser = pii
                players[pi][0] = yy
                players[pi][1] = xx
                players_cells[yy][xx] = pi
            else:
                winner = pii
                loser = pi
            
            players_point[winner] += point

            if players_gun[loser] != 0:
                guns[yy][xx].append(players_gun[loser])
                players_gun[loser] = 0
            
            direction = players[loser][2]
            yyy = yy + dy[direction]
            xxx = xx + dx[direction]
            while not (0 <= yyy < n and 0 <= xxx < n \
                and players_cells[yyy][xxx] == -1):
                direction = (direction + 1) % 4
                players[loser][2] = direction
                yyy = yy + dy[direction]
                xxx = xx + dx[direction]
                # 만약 4방에 사람이 있다면...?

            players[loser][0] = yyy
            players[loser][1] = xxx
            players_cells[yyy][xxx] = loser
            if guns[yyy][xxx]:
                most_powerful_gun = -1
                power = -1
                for gi in range(len(guns[yyy][xxx])):
                    if power < guns[yyy][xxx][gi]:
                        power = guns[yyy][xxx][gi]
                        most_powerful_gun = gi
                players_gun[loser] = power
                guns[yyy][xxx].pop(most_powerful_gun)
            
            if players_gun[winner] != 0:
                guns[yy][xx].append(players_gun[winner])
                players_gun[winner] = 0
            if guns[yy][xx]:
                most_powerful_gun = -1
                power = -1
                for gi in range(len(guns[yy][xx])):
                    if power < guns[yy][xx][gi]:
                        power = guns[yy][xx][gi]
                        most_powerful_gun = gi
                players_gun[winner] = power
                guns[yy][xx].pop(most_powerful_gun)
            

init()
for rounds in range(k):
    players_move()
print(*players_point)

# 1시간 35분