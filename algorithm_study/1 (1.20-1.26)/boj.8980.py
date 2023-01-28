import sys

# 마을 수, 트럭 용량
n, limit = map(int, input().split())
m = int(input())

loads = []
for _ in range(m):
    loads.append(tuple(map(int, sys.stdin.readline().rstrip().split())))

# loads.sort(key= lambda x: -(x[2] / (x[1] - x[0])))
loads.sort(key= lambda x: x[1])
# loads.sort(key= lambda x: ((x[1]-x[0]), x[0], -x[2]))
# loads.sort()
# print(*loads, sep='\n')

scheduler = [limit for _ in range(n)]
total = 0
for load in loads:
    start, end, amount = load
    maximum = amount
    for i in range(start, end):
        if maximum > scheduler[i]:
            maximum = scheduler[i] 
    for i in range(start, end):
        scheduler[i] -= maximum
    total += maximum
print(total)