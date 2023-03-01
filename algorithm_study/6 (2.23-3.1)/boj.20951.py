# 유아와 곰두리차
import sys
n, m = map(int, input().split())
g = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    g[a].append(b)
    g[b].append(a)

dp = [[0] * (n + 1) for _ in range(7 + 1)]
for i in range(n + 1):
    dp[1][i] = len(g[i])

for i in range(2, 7 + 1):
    for vi in range(1, n + 1):
        add = 0
        for gi in g[vi]:
            add += dp[i-1][gi]
        dp[i][vi] = add
    # print(dp[i])

print(sum(dp[7]) % (10 ** 9 + 7))


# 회차
# 0   1   2   3
# 1       1   1
# 2       1   1
# 3       1   1
# ...
# 7       1   1

# 회차
# 0   1   2   3   4
# 1   1   1   3   1
# 2   3   3   3   3
# 3   3   3   9   3
# 4