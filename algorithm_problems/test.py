t = int(input())

for tc in range(t):
    n = int(input())
    sticker = [list(map(int, input().split())) for _ in range(2)]
    dp = [[0] * (n) for _ in range(3)]
    dp[0][0] = sticker[0][0]
    dp[1][0] = sticker[1][0]
    dp[2][0] = 0
    for i in range(1, n):
        dp[0][i] = max(dp[1][i-1], dp[2][i-1]) + sticker[0][i]
        dp[1][i] = max(dp[0][i-1], dp[2][i-1]) + sticker[1][i]
        dp[2][i] = max(dp[0][i-1], dp[1][i-1])
    print(max(max(dp[0][n-1], dp[1][n-1]), dp[2][n-1]))





# [0][n]
# 이번꺼에서 위를 선택하는 최대값

# [1][n]
# 이번꺼에서 아래를 선택하는 최대값

# [2][n]
# 이번꺼에서 선택하지 않는 최대값