# 마법사 상어와 비바라기

import sys

dy = [0, 0, -1, -1, -1, 0, 1, 1, 1]
dx = [0, -1, -1, 0, 1, 1, 1, 0, -1]

n, m = map(int, sys.stdin.readline().rstrip().split())
A = [list(map(int, sys.stdin.readline().rstrip().split())) for i in range(n)]
clouds = []

def casting():
    clouds.append((n-1, 0))
    clouds.append((n-1, 1))
    clouds.append((n-2, 0))
    clouds.append((n-2, 1))

def step1(d, s):
    for i in range(len(clouds)):
        clouds[i] = ((clouds[i][0] + dy[d]*s)%n, (clouds[i][1] + dx[d]*s)%n)


def step2():
    for i in range(len(clouds)):
        y, x = clouds[i]
        A[y][x] += 1

def step3():
    for i in range(len(clouds)):
        for j in (2, 4, 6, 8):
            y, x = clouds[i]
            cellsHaveWater = 0
            if 0 <= y + dy[j] < n and 0 <= x + dx[j] < n:
                if A[y + dy[j]][x + dx[j]] > 0:
                    cellsHaveWater += 1
            A[y][x] += cellsHaveWater
     
def step4():
    global clouds
    newCloulds = set()
    temp = set(clouds)
    for y in range(n):
        for x in range(n):
            if A[y][x] >= 2:
                newCloulds.add((y, x))
    clouds = list(newCloulds - temp)
    for i in range(len(clouds)):
        y, x = clouds[i]
        A[y][x] -= 2

def moving(d: int, s: int):
    step1(d, s)
    step2()
    step3()
    step4()

casting()
for i in range(m):
    d, s = map(int, sys.stdin.readline().rstrip().split())
    moving(d, s)

ans = 0
for i in range(n):
    ans += sum(A[i])
print(ans)