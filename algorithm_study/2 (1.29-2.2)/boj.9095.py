# 1, 2, 3 더하기
t = int(input())

dp = [0 for i in range(11)]
dp[1] = 1
dp[2] = dp[1] + 1
dp[3] = dp[1] + dp[2] + 1

def sol(n):
    if dp[n] != 0:
        return dp[n]
    return sol(n - 3) + sol(n - 2) + sol(n - 1)

for _ in range(t):
    n = int(input())
    print(sol(n))