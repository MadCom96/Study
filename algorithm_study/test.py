n = int(input())
g = []
for i in range(n):
    g.append(list(map(int, input())))

inf = 1000000000000
shortest = [inf for i in range(n)]
shortest[1] = 0

def fix():
    