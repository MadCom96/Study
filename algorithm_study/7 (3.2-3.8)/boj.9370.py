# 미확인 도착지
# 시간을 3초나 주었다.
import sys
from heapq import *
input = sys.stdin.readline

inf = 1000 * 50000 + 1
graph = []

def dijkstra(node) -> list:
    global inf, graph
    node -= 1
    v = len(graph)
    d = graph[node][:]

    fixed = [False] * v
    fixed[node] = True
    isDone = True
    
    while True:
        shortest = inf
        shortest_idx = -1
        for i in range(n):
            isDone = isDone and fixed[i]
            if not fixed[i]:
                if d[i] < shortest:
                    shortest = d[i]
                    shortest_idx = i
        if shortest_idx == -1 or isDone:
            break
        fixed[shortest_idx] = True
        for i in range(n):
            if not fixed[i]:
                d[i] = min(d[i], d[shortest_idx] + graph[shortest_idx][i])
    return d


t = int(input())
for ti in range(t):
    n, m, t = map(int, input().split())
    s, g, h = map(int, input().split())

    graph = [[inf] * n for _ in range(n)]
    for i in range(n):
        graph[i][i] = 0
    for mi in range(m):
        a, b, d = map(int, input().split())
        graph[a-1][b-1] = d
        graph[b-1][a-1] = d

    dijk_sp = dijkstra(s)
    dijk_g = dijkstra(g)
    dijk_h = dijkstra(h)

    ans = []
    for ti in range(t):
        x = int(input())
        if dijk_sp[x-1] == min(
                dijk_sp[g-1] + graph[g-1][h-1] + dijk_h[x-1],
                dijk_sp[h-1] + graph[g-1][h-1] + dijk_g[x-1]):
            heappush(ans, x)
    while ans:
        print(heappop(ans), end=' ')
    print()

