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
    never[a] = True

visited = []
dq = deque()
def bfs(vertex) -> int:
    global visited, dq
    ans = 0
    while len(dq) != 0:
        a = dq.popleft()
        visited[a] = True
        ans += 1
        nexts = g[a]
        for ns in nexts:
            if not visited[ns]:
                dq.append(ns)
    return ans

highest = -1
highestList = []
i = 0
while i < n - 1:
    i += 1
    if never[i]:
        continue
    visited = [False for _ in range(n + 1)]
    dq = deque([i])
    connection[i] = bfs(i)
    if connection[i] > highest:
        highest = connection[i]
        highestList = [i]
    elif connection[i] == highest:
        highestList.append(i)

print(*highestList, sep=' ')