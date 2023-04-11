from copy import deepcopy

# 한변 크기, 도망자 수, 나무 수, 턴 수
n, m, h, k = map(int, input().split())

# 시작점 위치 y, x, catcher direction 0
y = n // 2
x = n // 2
cd = 0

# 움직이는 순서 만들어주기
nn = n * n - 1
move_order = []
moi = 0
moj = 0
cnt = 2
go = 1
while True:
    cnt -= 1
    if cnt == -1:
        go += 1
        cnt = 1
    
    move_order.append(min(go, nn))
    nn -= go
    if nn < 0:
        break

# 1 오른쪽 2 아래쪽
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

field = []
isTree = []
for i in range(n):
    l = []
    ll = []
    for j in range(n):
        l.append([])
        ll.append(False)
    field.append(l)
    isTree.append(ll)

for mi in range(m):
    yy, xx, d = map(int, input().split())
    field[yy-1][xx-1].append(d)

for hi in range(h):
    yy, xx = map(int, input().split())
    isTree[yy-1][xx-1] = True

def runners_move():
    global n, m, h, k, y, x, dy, dx, field, isTree
    line_runners = []
    for yy in range(y - 3, y + 3 + 1):
        if not 0 <= yy < n:
            continue
        diffLeft = 3 - abs(yy - y)
        for xx in range(x - diffLeft, x + diffLeft + 1):
            if not 0 <= xx < n:
                continue
            while field[yy][xx]:
                dd = field[yy][xx].pop(0)
                line_runners.append((yy, xx, dd))
    # print("움직인 사람 수:", len(line_runners))
    while line_runners:
        yy, xx, dd = line_runners.pop(0)
        yyy = yy + dy[dd]
        xxx = xx + dx[dd]
        if 0 <= yyy < n and 0 <= xxx < n:
            if y == yyy and x == xxx:
                field[yy][xx].append(dd)
            else: 
                field[yyy][xxx].append(dd)
        else:
            dd = (dd + 2) % 4
            yyy = yy + dy[dd]
            xxx = xx + dx[dd]
            if y == yyy and x == xxx:
                field[yy][xx].append(dd)
            else:
                field[yyy][xxx].append(dd)
                        
reversed_move_order = False
turns = 0
score = 0
def catcher_move():
    global n, m, h, k, y, x, cd, dy, dx, field, isTree, moi, moj, move_order, reversed_move_order, turn, score
    if not reversed_move_order:
        moj += 1
        y += dy[cd]
        x += dx[cd]
        if y == 0 and x == 0:
            cd = 2
            reversed_move_order = True
            moj = 0
        elif move_order[moi] == moj:
            moj = 0
            moi += 1
            cd = (cd + 1) % 4
    else:
        moj += 1
        y += dy[cd]
        x += dx[cd]
        if y == n // 2 and x == n // 2:
            cd = 0
            reversed_move_order = False
            moj = 0
        elif move_order[moi] == moj:
            moj = 0
            moi -= 1
            cd = (cd - 1) % 4
    # print(turns, "번째 턴")
    # print(*field, sep='\n')
    # print("현재 위치", y, x)
    # print("방향:", end=' ')
    # if cd == 0:
    #     print("위쪽")
    # elif cd == 1:
    #     print("오른쪽")
    # elif cd == 2:
    #     print("아래쪽")
    # elif cd == 3:
    #     print("왼쪽")

    for i in range(3):
        yy = y + dy[cd] * i
        xx = x + dx[cd] * i
        if not (0 <= yy < n and 0 <= xx < n):
            break
        if isTree[yy][xx]:
            continue
    #     print(yy, xx, "칸에서 점수", len(field[yy][xx]) * turns)
        score += len(field[yy][xx]) * turns
    #     print("현재 점수", score)
        field[yy][xx] = []
    #     print("field")
    #     print(*field, sep='\n')
    # print()
        
def turn():
    global turns
    turns += 1
    runners_move()
    catcher_move()

for i in range(k):
    turn()

print(score)
# 5 3 1 1
# 2 4 1
# 1 4 2
# 4 2 1
# 2 4

#    0
#   000
#  00000
# 0001000
#  00000
#   000
#    0