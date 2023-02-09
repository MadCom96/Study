# 주사위 굴리기
n, m, x, y, k = map(int, input().split())
maps = [list(map(int,input().split())) for _ in range(n)]
orders = list(map(int, input().split()))

dx = [0, 0, 0, -1, 1]
dy = [0, 1, -1, 0, 0]
# 동서북남

dice = [0] * 6
#   1
# 3 0 2
#   4
#   5
def roll_dice(direction):
    global dice
    if direction == 1:
        dice = [dice[3], dice[1], dice[0], dice[5], dice[4], dice[2]]
    elif direction == 2:
        dice = [dice[2], dice[1], dice[5], dice[0], dice[4], dice[3]]
    elif direction == 3:
        dice = [dice[4], dice[0], dice[2], dice[3], dice[5], dice[1]]
    elif direction == 4:
        dice = [dice[1], dice[5], dice[2], dice[3], dice[0], dice[4]]
    # print(f"  {dice[1]}  ")
    # print(f"{dice[3]} {dice[0]} {dice[2]}")
    # print(f"  {dice[4]}  ")
    # print(f"  {dice[5]}  ")

for order in orders:
    if 0 <= x + dx[order] < n and 0 <= y + dy[order] < m:
        pass
    else:
        continue
    x += dx[order] 
    y += dy[order]
    roll_dice(order)
    print(dice[0])
    # 이동한 칸에 쓰여 있는 수가 0이면, 주사위의 바닥면에 쓰여 있는 수가 칸에 복사
    if maps[x][y] == 0:
        maps[x][y] = dice[5]
    # 0이 아닌 경우에는 칸에 쓰여 있는 수가 주사위의 바닥면으로 복사되며, 칸에 쓰여 있는 수는 0이 된다.
    else:
        dice[5] = maps[x][y]
        maps[x][y] = 0