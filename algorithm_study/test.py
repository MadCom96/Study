# 우물
import sys
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
w = list(map(int, input().rstrip().split()))
g = [list(map(int, input().rstrip().split())) for _ in range(m)]

conn = [[] for i in range(n + 1)]
for gg in g:
    a = gg[0]
    b = gg[1]
    conn[a].append(b)
    conn[b].append(a)

print(*conn, sep='\n')