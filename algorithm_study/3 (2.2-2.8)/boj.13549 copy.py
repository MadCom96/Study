# 숨바꼭질 3
from collections import deque
n, k = map(int, input().split())

inf = 100001
lim = 200010

dist = [inf] * lim
dist[n] = 0

dq = deque()
dq.append(n)

while len(dq) != 0:
    current = dq.popleft()

    if current == k:
        print(dist[k])
        break

    warp = current * 2
    
    if warp < lim and dist[warp] > dist[current]:
        dist[warp] = dist[current]
        dq.appendleft(warp)
    if 0 <= current - 1 < lim:
        if dist[current - 1] > dist[current] + 1:
            dq.append(current - 1)
            dist[current - 1] = dist[current] + 1
    if 0 <= current + 1 < lim:
        if dist[current + 1] > dist[current] + 1:
            dq.append(current + 1)
            dist[current + 1] = dist[current] + 1

# 0-1 bfs 풀이