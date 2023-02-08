# 최단경로
import sys
from heapq import *
input = sys.stdin.readline

v, e = map(int, input().rstrip().split())
k = int(input())
inf = 2 ** 30 - 1
graph = [[inf for i in range(v + 1)] for i in range(v + 1)]
for _ in range(e):
    fromV, toV, w = map(int, input().rstrip().split())
    graph[fromV][toV] = min(graph[fromV][toV], w)

dijkstra = [inf for _ in range(v + 1)]
dijkstra[k] = 0

dheapq = []
# (거리, 어떤 위치)
heappush(dheapq, (0, k))

while len(dheapq) != 0:
    length, fromV = heappop(dheapq)
    # 현재 가장 짧은 거리를 반환받는다.
    if dijkstra[fromV] < length:
        continue

    for toV in range(1, v + 1):
        if graph[fromV][toV] == inf:
            continue
        nextV = dijkstra[fromV] + graph[fromV][toV]
        if nextV < dijkstra[toV]:
            dijkstra[toV] = nextV
            heappush(dheapq, (nextV, toV))

for i in range(1, v + 1):
    if dijkstra[i] == inf:
        print("INF")
    else:
        print(dijkstra[i])

# 메모리초과코드