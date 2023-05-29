from copy import deepcopy

n, m, k, c = map(int, input().split())
# 격자의 크기, 박멸 진행 년 수, 제초제 확산범위, 제초제 남아있는 년 수
# 5~20,     1~1000,       1~20         1~10
cells = [list(map(int, input().split())) for _ in range(n)]
# 나무 그루 수, 벽의 정보
# 1 ~ 100 나무, 0 빈 칸, -1 벽
weeded = [[0] * n for _ in range(n)]

dy = [-1, -1, 0, 1, 1, 1, 0, -1]
dx = [0, 1, 1, 1, 0, -1, -1, -1]
adjacent = (0, 2, 4, 6)
diagonal = (1, 3, 5, 7)

ans = 0

# 인접한 네 개의 칸 중 나무가 있는 칸의 수만큼 나무가 성장합니다. 성장은 모든 나무에게 동시에 일어납니다.
def tree_growth():
    global n, m, k, c, cells, weeded, dy, dx, adjacent, diagonal
    cells_next = deepcopy(cells)
    for y in range(n):
        for x in range(n):
            if not cells[y][x] > 0:
                continue
            for d in adjacent:
                yy = y + dy[d]
                xx = x + dx[d]
                if not (0 <= yy < n and 0 <= xx < n):
                    continue
                if cells[yy][xx] > 0:
                    cells_next[y][x] += 1
    cells = cells_next

# 기존에 있었던 나무들은 인접한 4개의 칸 중 벽, 다른 나무, 제초제 모두 없는 칸에 번식을 진행합니다
def tree_breeding():
    global n, m, k, c, cells, weeded, dy, dx, adjacent, diagonal
    cells_next = deepcopy(cells)
    for y in range(n):
        for x in range(n):
            if not cells[y][x] > 0:
                continue
            breed_to = []
            for d in adjacent:
                yy = y + dy[d]
                xx = x + dx[d]
                if not (0 <= yy < n and 0 <= xx < n):
                    continue
                if cells[yy][xx] == 0 and weeded[yy][xx] == 0:
                    breed_to.append((yy, xx))
            
            if len(breed_to) != 0:
                amount = cells[y][x] // len(breed_to)
            for yyy, xxx in breed_to:
                cells_next[yyy][xxx] += amount
    cells = cells_next

# 각 칸 중 제초제를 뿌렸을 때 나무가 가장 많이 박멸되는 칸에 제초제를 뿌립니다
def weeding():
    global n, m, k, c, cells, weeded, dy, dx, adjacent, diagonal, ans

    for y in range(n):
        for x in range(n):
            if weeded[y][x] != 0:
                weeded[y][x] += 1
                if weeded[y][x] == c + 1:
                    weeded[y][x] = 0

    most_effective = [(0, 0)]
    how_effective = 0
    # 행이 작은 순서, 열이 작은 순서. y, x를 바꿀 가능성 있음
    for y in range(n):
        for x in range(n):
            if cells[y][x] <= 0:
                continue
            total = cells[y][x]
            add_weeding_to = [(y, x)]
            for d in diagonal:
                i = 1
                while True:
                    if i > k:
                        break
                    yy = y + dy[d] * i
                    xx = x + dx[d] * i
                    if not (0 <= yy < n and 0 <= xx < n):
                        break
                    total += max(cells[yy][xx], 0)
                    add_weeding_to.append((yy, xx))
                    if cells[yy][xx] <= 0:
                        break
                    i += 1
            
            if how_effective < total:
                how_effective = total
                most_effective = add_weeding_to

    ans += how_effective
    for y, x in most_effective:
        if cells[y][x] != -1:
            cells[y][x] = 0
        weeded[y][x] = 1


for year in range(m):
    tree_growth()
    tree_breeding()
    weeding()

print(ans)

# 1시간 10분