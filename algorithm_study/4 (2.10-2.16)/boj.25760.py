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

cars_init = list(map(int, input().split()))
cars_init.insert(0, 0)

depths = []

parents = deque([0])
bfs = deque([1])
depthDQ = deque([0])
while bfs:
    p = parents.popleft()
    node = bfs.popleft()
    dd = depthDQ.popleft()
    if cars_init[node] == 1:
        depths.append(dd)
    for c in conn[node]:
        if c == p:
            continue
        parents.append(node)
        bfs.append(c)
        depthDQ.append(dd + 1)

# print(depths)

lencars = len(depths)
cnt = 0
ans = 0
# bfs를 해서 깊이를 구했으므로 깊이가 길수록 뒤에 있을 수 밖에 없다.
# 이를 역순으로 돌린다면 멀리있는 차를 먼저 보낸다는 가정을 할수있다.
for i in range(lencars-1, -1, -1):
    cnt += 1
    time = cnt + depths[i]
    if time > ans:
        ans = time
print(ans)