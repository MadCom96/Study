# 정전
n, l = map(int, input().split())
loc = list(map(int, input().split()))
loc.sort()
loc.insert(0, loc[0] - 2 * l - 1)


ans = 0
for i in range(2, n + 1):
    ans += max(loc[i-1] + l - max(loc[i] - l, loc[i-2] + l), 0)
print(ans)


# 점  겹  정겹  정?
# -6  0   0
# -2  0   2   v
# 1   