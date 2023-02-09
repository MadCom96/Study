# 점프 점프
n = int(input())
aList = list(map(int, input().split()))

inf = 1000 * 101

dp = [inf] * n
dp[0] = 0

for i in range(n):
    a = aList[i]
    for di in range(i + 1, i + a + 1):
        if di >= n:
            break
        dp[di] = min(dp[di], dp[i] + 1)

if dp[-1] == inf:
    print(-1)
else:
    print(dp[-1])