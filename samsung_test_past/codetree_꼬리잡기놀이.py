n, m, k = map(int, input().split())
# 0 빈칸, 1 머리사람, 2 나머지, 3 꼬리사람, 4 이동선
lines = [list(map(int, input().split())) for _ in range(n)]
heads = [] 
for y in range(n):
    for x in range(n):
        if lines[y][x] == 1:
            heads.append((y, x))

dy = [0, -1, 0, 1]
dx = [1, 0, -1, 0]
round = 0
score = 0
head_tail_change = [0, 0]

def each_team_move():
    global n, m, k, lines, heads, dy, dx
    for hi in range(len(heads)):
        y, x = heads[hi]
        for d in range(4):
            yy = y + dy[d]
            xx = x + dx[d]
            if not (0 <= yy < n and 0 <= xx < n):
                continue
            if lines[yy][xx] == 4 or lines[yy][xx] == 3:
                heads[hi] = (yy, xx)
                lines[yy][xx] = 1
                exception = d
                yy = y
                xx = x
                while True:
                    flag = False
                    for dd in range(4):
                        if dd == exception:
                            continue
                        yyy = yy + dy[dd]
                        xxx = xx + dx[dd]
                        if not (0 <= yyy < n and 0 <= xxx < n):
                            continue
                        if lines[yyy][xxx] == 0:
                            continue
                        if lines[yyy][xxx] == 1:
                            lines[yy][xx] = 3
                            flag = True
                            break
                        if lines[yyy][xxx] == 3:
                            lines[yy][xx] = 3
                            lines[yyy][xxx] = 4
                            flag = True
                            break
                        if lines[yyy][xxx] == 2:
                            lines[yy][xx] = 2
                            yy = yyy
                            xx = xxx
                            exception = (dd + 2) % 4
                            break
                    if flag:
                        break
                break

def dfs(y, x, exception, depth):
    global n, m, k, lines, heads, dy, dx, round, score, head_tail_change
    if lines[y][x] == 1:
        head_tail_change[0] = (y, x)
        return depth
    elif lines[y][x] == 3:
        head_tail_change[1] = (y, x)
        return 0

    for d in range(4):
        if d == exception:
            continue
        yy = dy[d] + y
        xx = dx[d] + x
        if not (0 <= yy < n and 0 <= xx < n):
            continue
        if lines[yy][xx] != 0 and lines[yy][xx] != 4:
            return dfs(yy, xx, (d + 2) % 4, depth + 1)


def score_calculate(y, x):
    global n, m, k, lines, heads, dy, dx, round, score, head_tail_change
    loc1 = (-1, -1)
    loc2 = (-1, -1)
    head_tail_change = [0, 0]
    if lines[y][x] == 1:
        loc1 = (y, x)
        score += 1
        # print("1 번째 사람")
        # print("1 점 적립 후", score, '점')
        for d in range(4):
            yy = y + dy[d]
            xx = x + dx[d]
            if not (0 <= yy < n and 0 <= xx < n):
                continue
            if lines[yy][xx] == 2 or lines[yy][xx] == 3:
                dfs(yy, xx, (d + 2) % 4, 2)
                break
        loc2 = head_tail_change[1]

    elif lines[y][x] == 3:
        loc2 = (y, x)
        for d in range(4):
            yy = y + dy[d]
            xx = x + dx[d]
            if not (0 <= yy < n and 0 <= xx < n):
                continue
            if lines[yy][xx] == 2:
                ppl = dfs(yy, xx, (d + 2) % 4, 2)
                score += ppl ** 2
                # print(ppl, "번째 사람")
                # print(ppl**2, "점 적립 후", score, '점')
                break
        if head_tail_change[0] == 0:
            for d in range(4):
                yy = y + dy[d]
                xx = x + dx[d]
                if not (0 <= yy < n and 0 <= xx < n):
                    continue
                if lines[yy][xx] == 1:
                    ppl = dfs(yy, xx, (d + 2) % 4, 2)
                    score += ppl ** 2
                    # print(ppl, "번째 사람")
                    # print(ppl**2, "점 적립 후", score, '점')
                    break

        loc1 = head_tail_change[0]
    
    else:
        for d in range(4):
            yy = y + dy[d]
            xx = x + dx[d]
            if not (0 <= yy < n and 0 <= xx < n):
                continue
            if lines[yy][xx] != 0 and lines[yy][xx] != 4:
                ppl = dfs(yy, xx, (d + 2) % 4, 2)
                score += ppl ** 2
                # print(ppl, "번째 사람")
                # print(ppl**2, "점 적립 후", score, '점')
        loc1 = head_tail_change[0]
        loc2 = head_tail_change[1]
    # print('head:', loc1)
    # print('tail:', loc2)
    # print('방향 바꿈')
    
    lines[loc1[0]][loc1[1]], lines[loc2[0]][loc2[1]] = lines[loc2[0]][loc2[1]], lines[loc1[0]][loc1[1]]
    for hi in range(len(heads)):
        if heads[hi] == loc1:
            heads[hi] = loc2
    # print(*lines, sep='\n')
    # print(heads)

def throw_ball():
    global n, m, k, lines, heads, dy, dx, round, score
    direction = (round - 1) // n
    direction %= 4
    nth = (round - 1) % n
    y = 0
    x = 0
    if direction == 0:
        y = nth
    elif direction == 1:
        y = n - 1
        x = nth
    elif direction == 2:
        x = n - 1
        y = n - 1 - nth
    else:
        x = n - 1 - nth
  
    d = direction
    # print(y, x, '에서 던짐')
    while 0 <= y < n and 0 <= x < n:
        if lines[y][x] != 0 and lines[y][x] != 4:
            score_calculate(y, x)
            break
        y += dy[d]
        x += dx[d]
    # print(y, x, '에서 부딪힘')

def round_steps():
    each_team_move()
    # print('이동 후')
    # print(*lines, sep='\n')
    throw_ball()

for _ in range(k):
    # input()
    round += 1
    # print(round, '번째 라운드')
    round_steps()
print(score)