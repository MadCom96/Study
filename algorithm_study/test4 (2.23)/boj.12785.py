# 토쟁이의 등굣길
w, h = map(int, input().split())
x, y = map(int, input().split())
# 1,1 에서 x, y를 거쳐 w h 까지

dp = [[0 for _ in range(y)] for _ in range(x)]
dp[0][0] = 1

for i in range(x):
    for j in range(y):
        if j > 0:
            dp[i][j] += dp[i][j - 1]
        if i > 0:
            dp[i][j] += dp[i - 1][j]

ans = dp[-1][-1]

dp = [[0 for _ in range(h - y + 1)] for _ in range(w - x + 1)]
dp[0][0] = ans

for i in range(w - x + 1):
    for j in range(h - y + 1):
        if j > 0:
            dp[i][j] += dp[i][j - 1]
        if i > 0:
            dp[i][j] += dp[i - 1][j]

print(dp[-1][-1] % 1000007)