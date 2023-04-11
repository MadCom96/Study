from collections import deque

n = int(input())
colors = [list(map(int,input().split())) for _ in range(n)]


dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]

entries = []
visited = []
checked = []

def bfs(y, x, mode):
    global n, colors, dy, dx, entries, visited, checked, entries
    if mode == 'leaveEntryMode':
        dq = deque([(y, x)])
        color = colors[y][x]
        visited[y][x] = True
        checked[y][x] = True
        cnt = 1
        while dq:
            y, x = dq.popleft()
            for i in range(4):
                yy = y + dy[i]
                xx = x + dx[i]
                if 0 <= yy < n and 0 <= xx < n:
                    if visited[yy][xx]:
                        continue
                    if colors[yy][xx] == color:
                        visited[yy][xx] = True
                        checked[yy][xx] = True
                        dq.append((yy, xx))
                        cnt += 1
                    else:
                        entries.append((yy,xx))
        return color, cnt

    elif mode == 'checkMode':
        dq = deque([(y, x)])
        color = colors[y][x]
        checked[y][x] = True
        border = 0
        cnt = 1
        while dq:
            y, x = dq.popleft()
            for i in range(4):
                yy = y + dy[i]
                xx = x + dx[i]
                if 0 <= yy < n and 0 <= xx < n:
                    if visited[yy][xx] and checked[yy][xx]:
                        border += 1
                        continue
                    if checked[yy][xx]:
                        continue
                    if colors[yy][xx] == color:
                        checked[yy][xx] = True
                        dq.append((yy, xx))
                        cnt += 1
        return color, cnt, border

def art_score():
    global n, colors, dy, dx, entries, visited, checked
    visited = [[False] * n for _ in range(n)]
    score = 0
    for y in range(n):
        for x in range(n):
            if visited[y][x]:
                continue
            checked = [[False] * n for _ in range(n)]
            num1, cells1 = bfs(y, x, 'leaveEntryMode')
            while entries:
                yy, xx = entries.pop(0)
                if checked[yy][xx]:
                    continue
                num2, cells2, border = bfs(yy, xx, 'checkMode')
                score += (cells1 + cells2) * num1 * num2 * border
    return score

def swap(y1, x1, y2, x2):
    global colors
    colors[y1][x1], colors[y2][x2] = colors[y2][x2], colors[y1][x1]

# 1 왼쪽 위, 2 오른쪽 아래
def rotate_div(y1, x1, y2, x2):
    global colors
    tmp = []
    for x in range(x1, x2):
        line = []
        for y in range(y2 - 1, y1 - 1, -1):
            line.append(colors[y][x])
        tmp.append(line)
    for y in range(y1, y2):
        for x in range(x1, x2):
            colors[y][x] = tmp[y - y1][x - x1]


def rotate():
    global n, colors, dy, dx, entries, visited, checked
    mid = n // 2
    for i in range(1, n//2 + 1):
        swap(mid, mid-i, mid-i, mid)
        swap(mid-i, mid, mid, mid+i)
        swap(mid, mid+i, mid+i, mid)
    
    rotate_div(0, 0, mid, mid)
    rotate_div(0, mid+1, mid, n)
    rotate_div(mid+1, 0, n, mid)
    rotate_div(mid+1, mid+1, n, n)

ans = 0
ans += art_score()
rotate()
ans += art_score()
rotate()
ans += art_score()
rotate()
ans += art_score()
print(ans)