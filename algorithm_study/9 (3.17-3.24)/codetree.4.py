# Sam의 피자학교
from copy import deepcopy

n, k = map(int, input().split())
flour = [list(map(int, input().split()))]

def step1():
    global n, flour
    least = 3001
    least_ind = []
    for fi in range(n):
        if flour[0][fi] < least:
            least = flour[0][fi]
            least_ind = [fi]
        elif flour[0][fi] == least:
            least_ind.append(fi)
    
    for li in least_ind:
        flour[0][li] += 1

def cutNlotate(y, x):
    global flour
    b = flour[-1][x:]
    ans = []
    for xi in range(x):
        line = []
        for yi in range(y-1, -1, -1):
            line.append(flour[yi][xi])
        ans.append(line)
    ans.append(b)
    flour = ans

def step2():
    y, x = 1, 1
    while True:
        yy = x + 1
        xx = y
        if n - (y * x) < xx:
            break
        cutNlotate(y, x)
        y = yy
        x = xx   
    

dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]
def step3():
    global dy, dx, flour
    flour_next = deepcopy(flour)
    for y in range(len(flour)):
        for x in range(len(flour[y])):
            for i in range(4):
                yy = y + dy[i]
                xx = x + dx[i]
                if (0 <= yy < len(flour) - 1 and 0 <= xx < len(flour[0])) \
                    or (yy == len(flour) - 1 and 0 <= xx < len(flour[-1])):
                    diff = flour[y][x] - flour[yy][xx]
                    diff //= 5
                    diff = max(diff, 0)
                    flour_next[y][x] -= diff
                    flour_next[yy][xx] += diff
    flour = flour_next
    line = []
    for xi in range(len(flour[0])):
        for yi in range(len(flour) - 1, -1, -1):
            line.append(flour[yi][xi])
    for xi in range(len(flour[0]), len(flour[-1])):
        line.append(flour[-1][xi])
    flour = [line]

def step4():
    global n, flour
    flour = flour[0]
    size = n//4
    a, b, c, d = flour[ : size], flour[size : 2*size], flour[2*size : 3*size], flour[3*size:]
    a.reverse()
    c.reverse()
    flour = [c, b, a, d]

def step5():
    step3()

def turn():
    step1()
    step2()
    step3()
    step4()
    step5()

cnt = 0
while True:
    least = 3000 * n
    best = 0
    for ff in flour[0]:
        if ff > best:
            best = ff
        if ff < least:
            least = ff
    ans =  best - least
    if ans <= k:
        print(cnt)
        break
    turn()
    cnt += 1