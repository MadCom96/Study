# 숨바꼭질 3
from heapq import *
n, k = map(int, input().split())

inf = 100001
lim = 200010
dijkstra = [inf] * lim
dijkstra[n] = 0

dheap = [(0, n)]

while len(dheap) != 0:
    time, fromV = heappop(dheap)
    print(n, "에서", fromV, "까지", time) 
    if fromV == k:
        print(time)
        break
    if time > dijkstra[fromV]:
        continue
    
    if 0 <= fromV - 1 < lim:
        dijkstra[fromV - 1] = min(dijkstra[fromV - 1], time + 1)
        heappush(dheap, (time + 1, fromV - 1))
    if 0 <= fromV + 1 < lim:
        dijkstra[fromV + 1] = min(dijkstra[fromV + 1], time + 1)
        heappush(dheap, (time + 1, fromV + 1))
    if 0 < fromV * 2 < lim:
        if abs(k - fromV) >= abs(k - fromV * 2):
            dijkstra[fromV * 2] = min(dijkstra[fromV * 2], time)
            heappush(dheap, (time, fromV * 2))

# 다익스트라 풀이
# 내코드도 잘좀 읽고 문제도 잘좀 읽자...
# 0 포함한 시간을 계산해야됨을 아예 고려안하고 0 < 씀