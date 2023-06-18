dp = []
lim = 1000000007
def solution(n):
    dp = [0] * (n + 4)
    dp[0] = 1
    for i in range(n):
        dp[i] %= lim
        dp[i+1] += dp[i]
        dp[i+2] += dp[i]
    return dp[n] % lim