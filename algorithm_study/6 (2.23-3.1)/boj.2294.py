# 동전 2
n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]
coins = list(set(coins))
coins.sort()

inf = 1000000
dp = [inf] * (k + 1)
dp[0] = 0

for coin in coins:
    for i in range(k + 1):
        if dp[i] != inf and i + coin <= k:
            dp[i + coin] = min(dp[i + coin], dp[i] + 1)

if dp[k] == inf:
    print(-1)
else:
    print(dp[k])