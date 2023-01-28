# 상범 빌딩
import sys
from collections import deque
input = sys.stdin.readline

# 동 서 남 북 상 하
dx = [1, -1, 0, 0, 0, 0]
dy = [0, 0, 1, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

bfs = deque()
building = []

if __name__ == "__main__":
    while True:
        L, R, C = map(int, input().rstrip().split())

        building = [[0 for r in range(R)] for l in range(L)]
        bfs = deque()

        sNotFound = True
        if L == 0 and R == 0 and C == 0:
            break
        for l in range(L):
            for r in range(R):
                line = list(input().rstrip())
                if sNotFound:
                    for c in range(C):
                        if line[c] == 'S':
                            sNotFound = False
                            bfs.append((l, r, c, 0)) # 층, 세로, 가로, 시간 
                building[l][r] = line
            input()
        
        ans = -1
        while len(bfs) != 0:
            z, y, x, t = bfs.popleft()
            if building[z][y][x] == 'E':
                ans = t
                break

            for i in range(6):
                zz = z + dz[i]
                yy = y + dy[i]
                xx = x + dx[i]

                if -1 < zz < L:
                    if -1 < yy < R:
                        if -1 < xx < C:
                            if building[zz][yy][xx] == '.':
                                building[zz][yy][xx] = '#'
                                bfs.append((zz, yy, xx, t + 1))
                            elif building[zz][yy][xx] == 'E':
                                bfs.append((zz, yy, xx, t + 1))
        
        if ans == -1:
            print("Trapped!")
        else:
            print(f"Escaped in {ans} minute(s).")