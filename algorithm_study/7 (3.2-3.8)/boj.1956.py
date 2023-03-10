# 운동
import sys
input = sys.stdin.readline

inf = int(1e9)

v, e = map(int, input().split())

dist = [[inf] * v for _ in range(v)]
# for i in range(v):
#     dist[i][i] = 0
for _ in range(e):
    a, b, c = map(int, input().split())
    dist[a-1][b-1] = c
# print(*dist, sep='\n')
# print()

for k in range(v):
    for i in range(v):
        # if k == i or dist[i][k] == inf:
        #     continue
        for j in range(v):
            # if i == j or k == j or dist[k][j] == inf:
            #     continue
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
            # print(*dist, sep='\n')
            # print()

# print()
# for i in range(v):
#     for j in range(v):
#         if dist[i][j] >= inf:
#             dist[i][j] = 'inf'
#         print(f'{dist[i][j]:3}', end=' ')
#     print()

ans = inf
for i in range(v):
    ans = min(ans, dist[i][i])
if ans == inf:
    ans = -1
print(ans)