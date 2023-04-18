from copy import deepcopy

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.

n = 0

cells = []
points = []
lines = []

ans = [0, 0]

def check(DD, Y1, X1, Y2, X2):
    global n, points, lines
    for i in range(len(lines)):
        dd, y1, x1, y2, x2 = lines[i]
        if ((y1 <= Y2 and y2 >= Y1) or (y2 >= Y1 and y1 <= Y2)) and \
            ((x1 <= X2 and x2 >= X1) or (x2 >= X1 and x1 <= X2)):
            return False
    return True


def dfs(ith, cnt, length):
    global n, points, lines
    # 남은 모든 포인트가 연결되어도 최대연결수에 못미칠때
    if len(points) - ith + cnt < ans[0]:
        return
    # 남은 모든 포인트가 연결되면 갯수는 같으나 이미 길이가 더 길때
    elif len(points) - ith + cnt == ans[0] and length > ans[1]:
        return
    
    if ith == len(points):
        # simulation()
        if ans[0] < cnt:
            ans[0] = cnt
            ans[1] = length
        elif ans[0] == cnt and ans[1] > length:
            ans[0] = cnt
            ans[1] = length 
        return
    
    y, x = points[ith]
    if min(y, x) == 0 or max(y, x) == n-1:
        if check(0, y, x, y, x):
            lines.append((0, y, x, y, x))
            dfs(ith+1, cnt+1, length)
            lines.pop()
    else:
        # 오른쪽으로 선분
        if check(0, y, x, y, n-1):
            lines.append((0, y, x, y, n-1))
            dfs(ith+1, cnt + 1, length + n-1-x)
            lines.pop()
        # 왼쪽으로 선분
        if check(0, y, 0, y, x):
            lines.append((0, y, 0, y, x))
            dfs(ith+1, cnt+1, length + x)
            lines.pop()
        # 아래쪽으로 선분
        if check(0, y, x, n-1, x):
            lines.append((0, y, x, n-1, x))
            dfs(ith+1, cnt+1, length + n-1-y)
            lines.pop()
        # 위쪽으로 선분
        if check(0, 0, x, y, x):
            lines.append((0, 0, x, y, x))
            dfs(ith+1, cnt+1, length + y)
            lines.pop()
        # 연결 x
        if check(-1, y, x, y, x):
            lines.append((-1, y, x, y, x))
            dfs(ith+1, cnt, length)
            lines.pop()


def soluition(inputN):
    global n, cells, points, lines, ans
    ans = [0, 0]

    n = inputN
    cells = [list(map(int, input().split())) for _ in range(n)]
    points = []
    lines = []
    for y in range(n):
        for x in range(n):
            if cells[y][x] == 1:
                points.append((y, x))
    dfs(0, 0, 0)

for test_case in range(1, T + 1):
    soluition(int(input()))
    print(f'#{test_case} {ans[1]}')


# 백트래킹을 잘해야 될 것만 같은 문제
# 백트래킹으로 통과...
# 1767. [SW Test 샘플문제] 프로세서 연결하기