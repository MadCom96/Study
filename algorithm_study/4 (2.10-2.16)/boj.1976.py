# 트리의 지름
from collections import deque

n = int(input())
g = {}
for i in range(1, n + 1):
    g[i] = []

for _ in range(n - 1):
    a, b, c = map(int, input().split())
    g[a].append((b, c))
    g[b].append((a, c))

leaf_node = deque()
for i in range(1, n + 1):
    if len(g[i]) == 1:
        leaf_node.append(i)

bfs = deque()
visited = []
longest = 0
while len(leaf_node) != 0:
    node = leaf_node.popleft()

    visited = [False for _ in range(n + 1)]
    visited[node] = True

    bfs.clear()
    bfs.append((node, 0))
    while len(bfs) != 0:
        v, l = bfs.popleft()
        if l > longest:
            longest = l
        for conn in g[v]:
            if not visited[conn[0]]:
                visited[conn[0]] = True
                bfs.append((conn[0], l + conn[1]))
    

print(longest)