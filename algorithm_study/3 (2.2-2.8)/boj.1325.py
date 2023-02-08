# 효율적인 해킹
import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
g = [[] for _ in range(n + 1)]
never = [False for _ in range(n + 1)]
connection = [0 for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int,input().rstrip().split())
    g[b].append(a)

highest = 0
for i in range(1, n + 1):
    visited = [False for _ in range(n + 1)]
    visited[i] = True
    dq = deque([i])
    while len(dq) != 0:
        nowV = dq.popleft()
        connection[i] += 1
        for nextV in g[nowV]:
            if not visited[nextV]:
                visited[nextV] = True
                dq.append(nextV)
    if connection[i] > highest:
        highest = connection[i]

for i in range(1, n + 1):
    if connection[i] == highest:
        print(i, end=' ')