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

# ================dp가 아닌 풀이==========
# s_copy = s
# # 30버튼 없을때 최소 + 1(start)
# no30 = s // 600
# s %= 600
# no30 += s // 60
# s %= 60
# no30 += s // 10
# no30 += 1

# s = s_copy - 30
# # 30버튼 == start버튼일때 최소
# yes30 = s // 600
# s %= 600
# yes30 += s // 60
# s %= 60
# yes30 += s //30
# s %= 30
# yes30 += s // 10
# yes30 += 1

# print(min(no30, yes30))