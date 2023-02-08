# 우물
import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
w = list(map(int, input().rstrip().split()))
w.insert(0, 0)

# 루트노드를 0 (1을 연결시켜서) 로 만든다
graph = [[] for i in range(n + 1)]
graph[0].append(1)

for i in range(m):
    a, b = map(int,input().rstrip().split())
    graph[a].append(b)
    graph[b].append(a)

fix = [0 for i in range(n + 1)]


def fixSum(parent, now):
    ans = 0
    for nextV in graph[now]:
        if nextV != parent:
            ans += fix[nextV]
    return ans + fix[now]


def dfs(parent, now) -> int:
    for nextV in graph[now]:
        if nextV != parent:
            fix[now] = max(fix[now], dfs(now, nextV))
    return max(w[now] - fixSum(parent, now), 0)

dfs(0, 0)
print(sum(fix))