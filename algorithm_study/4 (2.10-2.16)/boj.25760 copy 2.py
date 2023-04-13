# 귀경길 교통상황을 알려드립니다
import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
conn = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b = map(int, input().split())
    conn[a].append(b)
    conn[b].append(a)

cars = list(map(int, input().split()))
cars.insert(0, 0)

parent = deque([0])
bfs = deque([1])
depths = deque([0])
tree = []
while bfs:
    p = parent.popleft()
    v = bfs.popleft()
    d = depths.popleft()
    if len(tree) <= d:
        tree.append([])
    tree[d].append(cars[v])
    for c in conn[v]:
        if c == p:
            continue
        parent.append(v)
        bfs.append(c)
        depths.append(d+1)

print(*tree, sep='\n')

ans = cars.count(1)
for tr in tree:
    if 1 in tr:
        continue
    else:
        ans += 1
print(ans)