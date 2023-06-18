from collections import defaultdict

n = int(input())
graph = [0] * (n+1)
for i in range(n):
    value = list(map(int, input().split()))
    key = value.pop(0)
    graph[key] = value

