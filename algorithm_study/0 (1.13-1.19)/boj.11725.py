# 트리의 부모 찾기
from collections import deque

n = int(input())
tree = {}
for i in range(1, n + 1):
    tree[i] = []

for i in range(n - 1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

ans = [-1 for i in range(n + 1)]

bfs = deque([1])
while len(bfs) != 0:
    parent = bfs.popleft()
    
    for child in tree[parent]:
        ans[child] = parent
        bfs.append(child)
        tree[child].remove(parent)

print(*ans[2:], sep="\n")