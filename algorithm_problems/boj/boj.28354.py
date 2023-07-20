# 링크 컷 토마토
import sys
from heapq import *
# 재채점 된다면 쉬디가 감염될때 day 설정이 잘못되진 않았는지 확인

input = sys.stdin.readline
print = sys.stdout.write
inf = sys.maxsize

# 토마토개수, 0일 연결쌍, 0일 익은 수, 연결상태변화횟수
n, m, k, q = map(int, input().split())
graph = [set() for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    # 1 <= a < b <= n
    graph[a].add(b)
    graph[b].add(a)

# k개 일 것
riped = map(int, input().split())
ripeday = [inf] * (n + 1)
pq = []
ischecked = [False] * (n + 1)
for r in riped:
    ripeday[r] = 0
    heappush(pq, (0, r))

changes = []
cidx = 0
for i in range(q):
    changes.append(tuple(map(int, input().split())))

day = 0
# 한 loop는 하루를 의미
while True:
    isinfected = False
    while pq and pq[0][0] <= day:
        _, node1 = heappop(pq)
        # 필요 여부?
        if ischecked[node1]:
            continue
        tmpgraphnode = set()
        while graph[node1]:
            node2 = graph[node1].pop()
            if ischecked[node2]:
                continue
            tmpgraphnode.add(node2)
            # 더 짧은 거리를 찾았을 때!
            # 갱신해준다. ripeday
            if ripeday[node2] > day + 1:
                ripeday[node2] = day + 1
                heappush(pq, (day+1, node2))
                isinfected = True
        graph[node1] = tmpgraphnode
        ischecked[node1] = True

    if isinfected:
        day += 1
    else:
        if cidx != q:
            day = changes[cidx][0]
        else:
            break

    while cidx != q and changes[cidx][0] <= day:
        t, a, b = changes[cidx]
        cidx += 1
        if a in graph[b]:
            graph[b].discard(a)
            graph[a].discard(b)
        else:
            graph[a].add(b)
            graph[b].add(a)
            if (ripeday[a] == inf and ripeday[b] != inf) \
                    or (ripeday[a] != inf and ripeday[b] == inf):
                ischecked[a] = False
                ischecked[b] = False
                heappush(pq, (ripeday[a], a))
                heappush(pq, (ripeday[b], b))


for i in range(1, n+1):
    print("%d " % (ripeday[i] if ripeday[i] != inf else -1))
