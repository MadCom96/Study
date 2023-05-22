from heapq import *

n, m = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(n)]

houses = []
chickens = []
for i in range(n):
    for j in range(n):
        if city[i][j] == 0:
            continue
        if city[i][j] == 1:
            houses.append((i, j))
        elif city[i][j] == 2:
            chickens.append((i, j))

chosen = []
shortest = m * (2 * n + 1) * len(houses)
def simulation():
    global n, m, houses, chickens, chosen, shortest
    # 현재까지 거리 > 최소거리 일땐 그만두고 종료
    total_len = 0
    for house in houses:
        hy, hx = house
        shortest1vsN = n*n
        for ci in chosen:
            cy, cx = chickens[ci]
            length = abs(hy-cy) + abs(hx-cx)
            if length < shortest1vsN:
                shortest1vsN = length
        total_len += shortest1vsN
        if total_len > shortest:
            return
    shortest = total_len

def dfs(last, ith):
    global n, m, houses, chickens, chosen, shortest
    if ith == m:
        simulation()
        return

    for i in range(last+1, len(chickens) - (m-ith-1)):
        chosen.append(i)
        dfs(i, ith+1)
        chosen.pop(-1)

dfs(-1, 0)
print(shortest)