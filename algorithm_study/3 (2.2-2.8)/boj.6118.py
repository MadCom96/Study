# 숨바꼭질
import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
g = [[] for _ in range(n + 1)]
dist = [-1 for _ in range(n + 1)]
dist[1] = 0
for _ in range(m):
    a, b = map(int, input().rstrip().split())
    g[a].append(b)
    g[b].append(a)

dq = deque()
dq.append(1)
mostFar = 0
farList = []
while len(dq) != 0:
    now = dq.popleft()
    nexts = g[now]
    for ns in nexts:
        if dist[ns] == -1:
            dist[ns] = dist[now] + 1
            if dist[now] + 1 > mostFar:
                mostFar = dist[now] + 1
                farList = [ns]
            elif dist[now] + 1 == mostFar:
                farList.append(ns)
            dq.append(ns)

print(min(farList), mostFar, len(farList))