# 배열 돌리기 6
n, r = map(int, input().split())
array = [list(map(int, input().split())) for _ in range(2**n)]

def c1(l):
    global n, array
    cell = 2 ** l
    for y in range(0, 2**n, cell):
        for x in range(0, 2**n, cell):
            for yy in range(cell//2):
                for xx in range(cell):
                    array[y+yy][x+xx], array[y+cell-1-yy][x+xx] = array[y+cell-1-yy][x+xx], array[y+yy][x+xx]

def c2(l):
    global n, array
    cell = 2 ** l
    for y in range(0, 2**n, cell):
        for x in range(0, 2**n, cell):
            for yy in range(cell):
                for xx in range(cell//2):
                    array[y+yy][x+xx], array[y+yy][x+cell-1-xx] = array[y+yy][x+cell-1-xx], array[y+yy][x+xx]

def c3(l):
    global n, array
    cell = 2 ** l
    tmp = [[0] * cell for _ in range(cell)]
    for y in range(0, 2**n, cell):
        for x in range(0, 2**n, cell):
            for yy in range(cell):
                for xx in range(cell):
                    tmp[xx][cell-1-yy] = array[y+yy][x+xx]
            for yy in range(cell):
                for xx in range(cell):
                    array[y+yy][x+xx] = tmp[yy][xx]
            
def c4(l):
    global n, array
    cell = 2 ** l
    tmp = [[0] * cell for _ in range(cell)]
    for y in range(0, 2**n, cell):
        for x in range(0, 2**n, cell):
            for yy in range(cell):
                for xx in range(cell):
                    tmp[cell-1-xx][yy] = array[y+yy][x+xx]
            for yy in range(cell):
                for xx in range(cell):
                    array[y+yy][x+xx] = tmp[yy][xx]

def change(y1, x1, y2, x2, cell):
    global n, array
    tmp = [[0] * cell for _ in range(cell)]
    for y in range(cell):
        for x in range(cell):
            tmp[y][x] = array[y1+y][x1+x]
    for y in range(cell):
        for x in range(cell):
            array[y1+y][x1+x] = array[y2+y][x2+x]
    for y in range(cell):
        for x in range(cell):
            array[y2+y][x2+x] = tmp[y][x]

def c5(l):
    global n, array
    cell = 2 ** l
    for y in range(0, 2**n // 2, cell):
        for x in range(0, 2**n, cell):
            change(y, x, 2**n - y - cell, x, cell)

def c6(l):
    global n, array
    cell = 2 ** l
    for y in range(0, 2**n, cell):
        for x in range(0, 2**n // 2, cell):
            change(y, x, y, 2**n - x - cell, cell)

def c7(l):
    global n, array
    cell = 2 ** l
    line = 2 ** n // cell
    for y in range(line // 2):
        for x in range(y, line-y-1):
            y1, x1 = y * cell, x * cell
            y2, x2 = x * cell, (line - 1 - y) * cell
            y3, x3 = (line - 1 - y) * cell, (line - 1 - x) * cell
            y4, x4 = (line - 1 - x) * cell, y * cell
            change(y1, x1, y2, x2, cell)
            change(y1, x1, y4, x4, cell)
            change(y4, x4, y3, x3, cell)

def c8(l):
    global n, array
    cell = 2 ** l
    line = 2 ** n // cell
    for y in range(line // 2):
        for x in range(y, line-y-1):
            y1, x1 = y * cell, x * cell
            y2, x2 = x * cell, (line - 1 - y) * cell
            y3, x3 = (line - 1 - y) * cell, (line - 1 - x) * cell
            y4, x4 = (line - 1 - x) * cell, y * cell
            change(y1, x1, y2, x2, cell)
            change(y2, x2, y3, x3, cell)
            change(y4, x4, y3, x3, cell)

defs = [c1, c2, c3, c4, c5, c6, c7, c8]

for _ in range(r):
    k, l = map(int, input().split())
    defs[k-1](l)

for lineofarray in array:
    print(*lineofarray)