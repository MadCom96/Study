# 연구소
from collections import deque

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

n, m = map(int, input().split()) # n 세로 m 가로
lab = [list(map(int, input().split())) for i in range(n)]

b = deque()

# 0은 빈칸, 1은 벽, 2는 바이러스
# 추가적으로 3은 임시 벽, 4는 임시 바이러스
for y in range(n):
    for x in range(m):
        if lab[y][x] == 2:
            b.append((y, x)) # (y, x) 페어 튜플을 저장한다.

lim = n * m

def check(num):
    y = num // m
    x = num % m
    if lab[y][x] == 0:
        return True
    return False


def setWall(*nums):
    for num in nums:
        y = num // m
        x = num % m
        lab[y][x] = 3


def clear():
    for y in range(n):
        for x in range(m):
            if lab[y][x] > 2:
                lab[y][x] = 0

totalAns = 0
for i in range(lim - 2):
    if not check(i):
        continue
    for j in range(i + 1, lim - 1):
        if not check(j):
            continue
        for k in range(j + 1, lim):
            if not check(k):
                continue
            setWall(i, j, k)
            bfs = deque(b)
            while len(bfs) != 0:
                y, x = bfs.popleft()
                for ii in range(4):
                    if 0 <= y + dy[ii] < n and 0 <= x + dx[ii] < m:
                        if lab[y + dy[ii]][x + dx[ii]] == 0:
                            lab[y + dy[ii]][x + dx[ii]] = 4
                            bfs.append((y + dy[ii], x + dx[ii]))
            ans = 0
            for y in range(n):
                ans += lab[y].count(0)
            if ans > totalAns:
                totalAns = ans
            clear()

print(totalAns)