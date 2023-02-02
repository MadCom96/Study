# 우물
import sys
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
w = list(map(int, input().rstrip().split()))
g = [list(map(int, input().rstrip().split())) for _ in range(m)]

w.insert(0, 0)

conn = [[] for i in range(n + 1)]
for gg in g:
    a = gg[0]
    b = gg[1]
    conn[a].append(b)
    conn[b].append(a)

print(*conn, sep='\n')

dp = [0 for i in range(n + 1)]
satisfied = [False for i in range(n + 1)]

for i in range(1, n + 1):
    if len(conn[i]) == 1:
        dp[conn[i][0]] = w[i]

print(dp)

def needMore(v):
    total = dp[v]
    for c in conn[n]:
        total += dp[c]
    if total >= w[v]:
        return True
    return False

next = [0 for i in range(n + 1)]
highest = 0
highestIdx = 0
for v in range(1, n + 1):
    if needMore(v):
        satisfied[v] = True
    else:
        next[v] += 1
        if highest < next[v]:
            highest = next[v]
            highestIdx = v
        for nv in conn[v]:
            next[nv] += 1
            if highest < next[nv]:
                highest = next[nv]
                highestIdx = nv

while True:
    highestIdx


for v in range(1, n + 1):
    if satisfied[v] 