# 또 전자레인지야?
m, s = map(int, input().split(':'))
s += m * 60

dp = [100 for i in range((60 * 60 + 50) // 10 + 1)]
dp[1] = 2
dp[3] = 1
dp[6] = 2
dp[60] = 2

def fill_dp(s):
    for i in range(1, s // 10 + 1):
        if dp[i] == 100:
            if i > 1:
                dp[i] = min(dp[i], dp[i-1] + 1)
            if i > 3:
                dp[i] = min(dp[i], dp[i-3] + 1)
            if i > 6:
                dp[i] = min(dp[i], dp[i-6] + 1)
            if i > 60:
                dp[i] = min(dp[i], dp[i-60] + 1)
    return dp[s//10]

print(fill_dp(s))