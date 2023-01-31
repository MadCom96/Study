# 퇴사
n = int(input())

works = [[0, 0]]
dp = [0]

def fill_dp(i):
    dp.append(dp[i - 1])
    for j in range(i, 0, -1):
        if j + works[j][0] - 1 == i:
            dp[i] = max(dp[i], dp[j - 1] + works[j][1])

for i in range(1, n + 1):
    works.append(tuple(map(int, input().split())))
    fill_dp(i)

print(dp[n])