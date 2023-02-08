# 섬의 개수
import sys
from collections import deque
input = sys.stdin.readline

dx = [-1, 0, 1, 1, 1, 0, -1, -1]
dy = [-1, -1, -1, 0, 1, 1, 1, 0]

jido = []
dq = deque()
def bfs(y, x, h, w):
    dq = deque([(y, x)])
    while len(dq) != 0:
        y, x = dq.popleft()
        for i in range(8):
            if 0 <= y + dy[i] < h:
                if 0 <= x + dx[i] < w:
                    if jido[y+dy[i]][x+dx[i]] == 1:
                        jido[y+dy[i]][x+dx[i]] = 2
                        dq.append((y+dy[i], x+dx[i]))
                    
while True:
    w, h = map(int, input().rstrip().split())
    if w == h == 0:
        break

    jido = []
    for _ in range(h):
        jido.append(list(map(int, input().rstrip().split())))
    
    ans = 0
    for y in range(h):
        for x in range(w):
            if jido[y][x] == 1:
                ans += 1
                bfs(y, x, h, w)
    print(ans)