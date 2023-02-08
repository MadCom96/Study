# 특정한 최단 경로
import sys
from heapq import *
input = sys.stdin.readline

n, e = map(int, input().rstrip().split()) 
g = [[] for i in range(n + 1)]
for _ in range(e):
    a, b, c = map(int, input().rstrip().split())
    g[a].append((b, c))
    g[b].append((a, c))

v1, v2 = map(int, input().rstrip().split())

inf = 2 ** 30 - 1
def dijkstra(fromV, toV) -> int:
    dheap = [(0, fromV)]
    dijkstra = [inf] * (n + 1)
    dijkstra[fromV] = 0
    while len(dheap) != 0:
        nowL, fV = heappop(dheap)
        if fV == toV:
            return nowL
        if nowL > dijkstra[fV]:
            continue
        for tV, w in g[fV]:
            if dijkstra[tV] > nowL + w:
                dijkstra[tV] = nowL + w
                heappush(dheap, (nowL + w, tV))
    return dijkstra[toV]

ans = 0

loads = [[dijkstra(1, v1), dijkstra(1, v2)], dijkstra(v1, v2), [dijkstra(v2, n), dijkstra(v1, n)]]
compare = []
if loads[1] == inf:
    pass
else:
    if loads[0][0] != inf and loads[2][0] != inf:
        compare.append(loads[0][0] + loads[1] + loads[2][0])
    if loads[0][1] != inf and loads[2][1] != inf:
        compare.append(loads[0][1] + loads[1] + loads[2][1])
        # 실화냐... loads[2][0] 오타로 틀림
if len(compare) == 0:
    print(-1)
else:
    print(min(compare))

