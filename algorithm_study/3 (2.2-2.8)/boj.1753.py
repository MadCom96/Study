# 최단경로
import sys
from heapq import *
input = sys.stdin.readline

v, e = map(int, input().rstrip().split())
k = int(input())
graph = [[] for i in range(v + 1)]
for _ in range(e):
    fromV, toV, w = map(int, input().rstrip().split())
    graph[fromV].append((toV, w))

inf = 2 ** 30 - 1
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

    for toV, w in graph[fromV]:
        # nextV = fromV를 거쳐서 toV까지 간 것
        nextV = dijkstra[fromV] + w
        if nextV < dijkstra[toV]:
            dijkstra[toV] = nextV
            heappush(dheapq, (nextV, toV))

for i in range(1, v + 1):
    if dijkstra[i] == inf:
        print("INF")
    else:
        print(dijkstra[i])