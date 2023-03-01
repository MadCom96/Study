# 소형기관차
n = int(input()) # 50000 이하
big_cells = list(map(int, input().split())) # 각 객차. 100이하
big_cells.insert(0, 0)
lim = int(input()) # 소형기관차 최대 객차. n/3 보다 적다.

cell_sums = []
temp = 0
for i in range(0, n + 1):
    temp += big_cells[i]
    cell_sums.append(temp)

def total_cell(idx):
    global n, cell_sums, lim
    return cell_sums[idx] - cell_sums[idx - lim]

dp = [[0] * (n+1) for _ in range(3)]

# 1개 최대를 구한다.
for i in range(lim, n + 1):
    dp[0][i] = max(dp[0][i-1], total_cell(i))

# 2개 최대를 구한다.
for i in range(2*lim, n + 1):
    dp[1][i] = max(dp[1][i-1], total_cell(i) + dp[0][i-lim])

# 3개 최대를 구한다.
highest = 0
for i in range(3*lim, n + 1):
    dp[2][i] = max(dp[2][i-1], total_cell(i) + dp[1][i-lim])
    if dp[2][i] > highest:
        highest = dp[2][i]

print(dp[-1][-1])