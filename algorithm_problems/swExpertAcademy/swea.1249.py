from collections import deque

field = []
dp = []

T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    field = [list(map(int, input())) for _ in range(n)]
    dp = [[100001] * n for _ in range(n)]
    dp[0][0] = field[0][0]
    
    d = deque([(0, 0)])
    while d:
        y, x = d.popleft()
        for dy, dx in ((1, 0), (0, 1), (-1, 0), (0, -1)):
            yy = dy + y
            xx = dx + x
            if not (0 <= yy < n and 0 <= xx < n):
                continue 
            if dp[yy][xx] > dp[y][x] + field[yy][xx]:
                dp[yy][xx] = dp[y][x] + field[yy][xx]
                d.append((yy, xx))

    print(f'#{test_case} {dp[n-1][n-1]}')