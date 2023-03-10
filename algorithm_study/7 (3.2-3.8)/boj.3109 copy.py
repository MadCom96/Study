# 빵집
import sys
input = sys.stdin.readline

r, c = map(int, input().split())
lines = [list(input().rstrip()) for _ in range(r)]
for i in range(r):
    lines[i][0] = i + 1

dy = [-1, 0, 1]

now_group = []
next_group = [i for i in range(r)]
for x in range(c - 1):
    now_group = next_group
    next_group = []
    for y in now_group:
        for d in dy:
            if 0 <= d + y < r and lines[d+y][x+1] == '.':
                lines[d+y][x+1] = lines[y][x]
                next_group.append(d+y)
                break
    print()
    for i in range(r):
        for j in range(c):
            print(f'{lines[i][j]:>2}', end=' ')
        print()
print(len(next_group))