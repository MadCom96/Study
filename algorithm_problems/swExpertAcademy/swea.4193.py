# 수영대회 결승전(완전 탐색 + 구현)
# 파이썬 미지원 레전드 ㅋ
from collections import deque
q = deque()
t = deque()
pool = []
visited = []
end = ()

def dfs(y, x, time, ans) -> int:
    global pool, visited
    if (y, x) == end:
        ans = min(ans, time)
        return ans
    for dy, dx in ((1, 0), (0, 1), (-1, 0), (0, -1)):
        yy, xx = y+dy, x+dx
        if not(0 <= yy < n and 0 <= xx < n):
            continue
        if visited[yy][xx] or pool[yy][xx] == 1:
            continue
        if pool[yy][xx] == 2:
            visited[yy][xx] = True
            ans = dfs(yy, xx, (time // 3 + 1) * 3, ans)
            visited[yy][xx] = False
        else:
            visited[yy][xx] = True
            ans = dfs(yy, xx, time + 1, ans)
            visited[yy][xx] = False
    return ans
    


test_case = int(input())
for tc in range(test_case):
    n = int(input())
    pool = [list(map(int, input().split())) for _ in range(n)]
    start = tuple(map(int, input().split()))
    end = tuple(map(int, input().split()))

    visited = [[False] * n for _ in range(n)]
    visited[start[0]][start[1]] = True
    q = deque([start])
    t = deque([0])

    ans = dfs(start[0], start[1], 0, 10000000)

    if ans == 10000000:
        ans = -1
    print(f'#{tc+1} {ans}')