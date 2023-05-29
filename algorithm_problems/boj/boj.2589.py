# 보물섬
from collections import deque

r, c = map(int, input().split())
paper = [list(input()) for _ in range(r)]
lengths = []

longest = 0

dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]
def bfs(y, x):
    # 시작점을 받는다
    global r, c, paper, lengths, longest, dy, dx

    # lengths 초기화
    lengths = [[-1] * c for _ in range(r)]
    partly_longest = 0

    # bfs를 돌면서 길이 저장을 length에 해준다. 
    # 1) 0을 제외한 수는 visited 처럼 쓰인다. 
    # 2) 현재 점으로 부터 거리가 가장 긴 곳을 저장하여 함수가 끝날때 shortest 갱신
    q = deque([(y, x)])
    lengths[y][x] = 0
    while q:
        y, x = q.popleft()
        if partly_longest < lengths[y][x]:
            partly_longest = lengths[y][x]
        
        for i in range(4):
            yy = y + dy[i]
            xx = x + dx[i]
            # 범위검사
            if not (0 <= yy < r and 0 <= xx < c):
                continue
            # 육지검사
            if paper[yy][xx] == 'W':
                continue
            # if not visited[yy][xx] 역할
            if lengths[yy][xx] == -1:
                lengths[yy][xx] = lengths[y][x] + 1
                q.append((yy,xx))
    # print(f'{y} {x} 에서 출발한 최장거리\n{partly_longest}')
    if longest < partly_longest:
        longest = partly_longest

for i in range(r):
    for j in range(c):
        if paper[i][j] == 'L':
            bfs(i, j)

print(longest)