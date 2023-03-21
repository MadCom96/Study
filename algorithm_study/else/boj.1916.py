# 최소비용 구하기
import sys
from heapq import *
input = sys.stdin.readline

inf = sys.maxsize

n = int(input())
m = int(input())

buses = [[inf] * n for _ in range(n)]
for _ in range(m):
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1
    buses[a][b] = min(buses[a][b], c)
for i in range(n):
    buses[i][i] = 0

s, e = map(int, input().split())

def dijkstra(s, e):
    global inf, n, m, buses
    s -= 1
    e -= 1

    shortest = [inf] * n
    shortest[s] = 0
    fixed = [False] * n
    hq = [(0, s)]
    while hq and not fixed[e]:
        leng, from_v = heappop(hq)
        if fixed[from_v] or shortest[from_v] == inf:
            continue
        fixed[from_v] = True
        for i in range(n):
            if fixed[i]:
                continue
            if buses[from_v][i] != inf and shortest[i] > (leng + buses[from_v][i]):
                shortest[i] = leng + buses[from_v][i]
                heappush(hq, (shortest[i], i))
    return shortest[e]

print(dijkstra(s, e))