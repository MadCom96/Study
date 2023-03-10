# 플로이드
import sys
input = sys.stdin.readline

# inf 값은 100,000 * 100 보다는 커줘야 말이 된다...
inf = 1e9
# 도시의 개수
n = int(input())

dist = [[inf] * n for _ in range(n)]
for i in range(n):
    dist[i][i] = 0

# 버스의 개수
m = int(input())
for mi in range(m):
    a, b, c = map(int, input().split())
    dist[a - 1][b - 1] = min(c, dist[a-1][b-1])

for k in range(n):
    for i in range(n):
        if i == k or dist[i][k] == inf:
            continue
        for j in range(n):
            if i == k or k == j or dist[k][j] == inf:
                continue
            print(f'dist[{i}][{j}] = min(dist[{i}][{j}], dist[{i}][{k}] + dist[{k}][{j}])')
            print(f'dist[i][j] = min({dist[i][j]}, {dist[i][k]} + {dist[k][j]})')
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
            print(*dist, sep='\n')
            print()

for i in range(n):
    for j in range(n):
        if dist[i][j] >= inf:
            dist[i][j] = 0
        print(dist[i][j], end=' ')
    print()