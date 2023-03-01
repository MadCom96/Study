# 보석 도둑
import sys
from heapq import *
input = sys.stdin.readline

n, k = map(int, input().rstrip().split())
jewels = []
for _ in range(n):
    m, v = map(int, input().rstrip().split())
    heappush(jewels, (-v, m))

# 각 가방에는 보석을 최대 한개씩만 담을 수 있다.
backpacks = []
for _ in range(k):
    backpacks.append(int(input().rstrip()))
backpacks.sort()

ans = 0
while len(backpacks) != 0 and len(jewels) != 0:
    value, mass = heappop(jewels)
    value = -value

    l = 0
    r = len(backpacks)
    while l + 1 != r:
        m = (l + r) // 2
        if backpacks[m] > mass:
            r = m
        elif backpacks[m] == mass:
            l = m
            break
        else:
            l = m
    if backpacks[l] >= mass:
        ans += value
        backpacks.pop(l)
    elif r < len(backpacks) and backpacks[r] >= mass:
        ans += value
        backpacks.pop(r)
    else:
        pass
print(ans)

# 이분탐색 (시간초과)