is_used = [[False] * 7 for _ in range(7)]
dominos = []
visited = [[False] * 7 for _ in range(8)]
pieces = 0
cnt = 0

dy = [0, 1]
dx = [1, 0]

def dfs(y, x):
    global is_used, dominos, visited, pieces, cnt

    # 이미 검사된 칸일때
    if visited[y][x]:
        nextx = x + 1
        nexty = y + nextx // 7
        nextx %= 7
        dfs(nexty, nextx)
        return
    
    for i in range(2):
        yy = y + dy[i]
        xx = x + dx[i]
        # if y == 6 and x == 6 and yy == 7 and xx == 6:
        #     print()
        
        if not(yy < 8 and xx < 7): continue
        if visited[yy][xx]: continue
        if is_used[dominos[y][x]][dominos[yy][xx]]: continue

        visited[y][x] = True
        visited[yy][xx] = True
        is_used[dominos[y][x]][dominos[yy][xx]] = True
        is_used[dominos[yy][xx]][dominos[y][x]] = True
        pieces += 1

        if pieces == 28:
            cnt += 1
            visited[y][x] = False
            visited[yy][xx] = False
            is_used[dominos[y][x]][dominos[yy][xx]] = False
            is_used[dominos[yy][xx]][dominos[y][x]] = False
            pieces -= 1
            return

        nextx = x + 1
        nexty = y + nextx // 7
        nextx %= 7
        dfs(nexty, nextx)
        
        visited[y][x] = False
        visited[yy][xx] = False
        is_used[dominos[y][x]][dominos[yy][xx]] = False
        is_used[dominos[yy][xx]][dominos[y][x]] = False
        pieces -= 1

def main():
    global is_used, dominos, visited, cnt
    for _ in range(8):
        dominos.append(list(map(int,input())))
    dfs(0, 0)
    print(cnt)

main()