from heapq import *

n, m = map(int, input().split())
hq = []
for _ in range(m):
    a, b, c = map(int, input().split())
    heappush(hq, (c, (b, a)))
    