# 줄 세우기
n = int(input())
kids = list(map(int, input().split()))

# kidLoc = [0 for _ in range(len(kids) + 1)]
# for i in range(n):
#     kidLoc[kids[i]] = i + 1

# # 범위 전체는 n + 1, 마지막 원소 검사x (n+1)-1
# longestLine = 0
# temp = 0
# for i in range(1, n):
#     if kidLoc[i] < kidLoc[i+1]:
#         temp += 1
#     else:
#         if longestLine < temp:
#             longestLine = temp
#         temp = 0

# print(n - longestLine - 1)

# 내 앞에 연속되는 수가 몇개 있는지를 저장하는 dp를 사용하여 풀 수 있다.

dp = [0 for _ in range(n + 1)]
longest = 0
for k in kids:
    dp[k] = dp[k - 1] + 1
    longest = max(longest, dp[k])
print(longest)