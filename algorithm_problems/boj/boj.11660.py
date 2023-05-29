import sys
import copy
input = sys.stdin.readline

n, m = map(int, input().split())
nums = [list(map(int, input().split())) for _ in range(n)]
n += 1
nums.insert(0, [0] * n)
for i in range(1, n):
    nums[i].insert(0, 0)
sums = copy.deepcopy(nums)

for i in range(1, n):
    for j in range(1, n):
        sums[i][j] = sums[i][j-1] + sums[i-1][j] - sums[i-1][j-1] + nums[i][j]

for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    x1 -= 1
    y1 -= 1
    print(sums[x2][y2] - sums[x1][y2] - sums[x2][y1] + sums[x1][y1])