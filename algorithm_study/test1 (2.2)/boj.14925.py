# 목장 건설하기
m, n = map(int, input().split())
field = [list(input().split()) for _ in range(m)]

highest = 0
for y in range(m):
    for x in range(n):
        if field[y][x] == '0':
            if x == 0 or y == 0:
                field[y][x] = 1
            else:
                field[y][x] = min(min(field[y - 1][x - 1], field[y - 1][x]), field[y][x - 1]) + 1
            # 이부분 실수했다...
            if field[y][x] > highest:
                highest = field[y][x]
        else:
            field[y][x] = 0

print(highest)