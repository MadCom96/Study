# 보석 도둑
import sys
from heapq import *
input = sys.stdin.readline

n, k = map(int, input().rstrip().split())
jewels = []
for _ in range(n):
    m, v = map(int, input().rstrip().split())
    heappush(jewels, (-v, m))

bags = [int(input().rstrip()) for _ in range(k)]
bags.sort()

ans = 0
while len(jewels) != 0 and len(bags) != 0:
    value, mass = heappop(jewels)

    # 해당 보석을 담을 수 있는 가장 작은 가방
    # 보석 무게에 대한 upper bound를 실행해준다.
    l = 0
    r = len(bags)
    while l != r:
        m = (l + r) // 2
        if bags[m] == mass:
            r = m
            break
        elif bags[m] > mass:
            r = m
        else:
            l = m + 1
    if r < len(bags):
        ans += value
        bags.pop(r)
    else:
        pass

print(-ans)