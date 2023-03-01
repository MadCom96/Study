# 자두나무
t, w = map(int, input().split())

dp = [[[0 for k in range(t + 1)]for j in range(3)] for i in range(w + 1)]
drop_order = [0] * (t + 1)

for i in range(1, t + 1):
    drop_order[i] = int(input())

for i in range(w + 1):
    for j in range(1, t + 1):
        if i == 0:
            dp[i][1][j] = dp[i][1][j - 1]
            if drop_order[j] == 1:
                dp[i][1][j] += 1
        else:
            dp[i][1][j] = max(dp[i][1][j - 1], dp[i - 1][2][j - 1])
            if drop_order[j] == 1:
                dp[i][1][j] += 1
            dp[i][2][j] = max(dp[i][2][j - 1], dp[i - 1][1][j - 1])
            if drop_order[j] == 2:
                dp[i][2][j] += 1

ans = 0
for i in range(1, 3):
    for j in range(w + 1):
        ans = max(ans, dp[j][i][t])
print(ans)