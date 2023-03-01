# 색상환

N = int(input())
K = int(input())

dp = [[0 for i in range(1001)] for j in range(1001)]
# dp[a][b] -> a칸 색상환에서 b개를 선택하는 경우의 수

for n in range(1, N + 1):
    dp[n][1] = n

for k in range(2, K + 1):
    k2 = 2 * k
    if k2 <= 1000:
        dp[k2][k] = 2
    for n in range(k * 2 + 1, N + 1):
        dp[n][k] = dp[n - 1][k] + dp[n - 2][k - 1]
        dp[n][k] %= 1000000003

print(dp[N][K])