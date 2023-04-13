# 보석도둑
import sys
from heapq import *
input = sys.stdin.readline

n, k = map(int, input().split())

jewels = []
for _ in range(n):
    m, v = map(int, input().split())
    heappush(jewels, (m, v))

bags = []
for _ in range(k):
    c = int(input())
    heappush(bags, c)

mostExpensive = []
ans = 0
while bags and (jewels or mostExpensive):
    bag = heappop(bags)
    while jewels and jewels[0][0] <= bag:
        m, v = heappop(jewels)
        heappush(mostExpensive, -v)
    if mostExpensive:
        ans += heappop(mostExpensive)
    else:
        continue
print(-ans)