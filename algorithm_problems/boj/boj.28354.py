# 링크 컷 토마토import sys
from heapq import *

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



# infections이 진행되다가~~~
# 갑자기 멈춰!
# 그리고 10일부터 다시~~
#
# 감염
#  - 감염체크
#   - 감염이 있어!!
#    -> 다음날도 있을수도 있어 진행
#     - 다음날은 += 1
#   - 감염이 없어!!!!
#    -> 다음 변화까지 감염은 없겠군
#     - 다음날은 changes의 다음 원소
#
# while이 끝나는 조건?
#     더 이상의 변화가 없을 때!
#         노드 변화 없고 감염변화 없음
