# 퇴사 2
n = int(input())

works = [[0, 0]]
dp = [0]
checklist = {}

def fill_dp(i):
    dp.append(dp[i - 1])
    checkNext = i + works[i][0] - 1
    if checkNext not in checklist.keys():
        checklist[checkNext] = []
    checklist[checkNext].append(i)
    if i not in checklist.keys():
        return
    for check in checklist[i]:
        dp[i] = max(dp[i], dp[check - 1] + works[check][1])

for i in range(1, n + 1):
    works.append(tuple(map(int, input().split())))
    fill_dp(i)

print(dp[n])