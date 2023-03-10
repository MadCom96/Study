# 행성연결
from heapq import *
import sys
input = sys.stdin.readline

n = int(input().rstrip())
c = [list(map(int, input().rstrip().split())) for _ in range(n)]
parent = [i for i in range(n)]

hq = []

for y in range(n):
    for x in range(y + 1, n):
        heappush(hq, (c[y][x], y, x))

def find(node) -> int:
    global parent
    if parent[node] != node:
        parent[node] = find(parent[node])
    return parent[node]

def isCycle(y, x) -> bool:
    global parent
    yy = find(y)
    xx = find(x)
    if yy == xx:
        return True
    else:
        if yy != xx:
            parent[yy] = xx
        return False

ans = 0
edge = 0
while hq:
    w, y, x = heappop(hq)
    if not isCycle(y, x):
        ans += w
        edge += 1
        if edge == n - 1:
            break
# 테스트용
print(parent)
print(ans)
# 크루스칼 (+ 유니온파인드)