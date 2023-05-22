# 로봇청소기
n, m = map(int, input().split())
r, c, d = map(int , input().split())
room = [list(map(int, input().split())) for _ in range(n)]

# 북동남서
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

cnt = 0
def move():
    global n, m, r, c, d, room, dy, dx, cnt

    while True:
        # 1. 현재 칸이 아직 청소되지 않은 경우, 현재 칸을 청소한다.
        if room[r][c] == 0:
            room[r][c] = 2
            cnt += 1
        print(f'({r}, {c})... 방향 {d}')
        print(*room, sep='\n')
        input()

        # 2, 3번 판단
        have = False
        for di in range(4):
            y = r + dy[di]
            x = c + dx[di]
            if room[y][x] == 0:
                have = True
                break

        # 2. 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 없는 경우.
        if not have:
            y = r + dy[d-2]
            x = c + dx[d-2]
            if room[y][x] == 1:
                return
            r = y
            c = x
        # 3. 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 있는 경우.
        else:
            for _ in range(4):
                d = (d-1) % 4
                y = r + dy[d]
                x = c + dx[d]
                if room[y][x] == 0:
                    r = y
                    c = x
                    break

move()
print(cnt)