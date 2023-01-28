# 센서
n = int(input())
k = int(input())

sensors = list(set(map(int, input().split())))
sensors.sort()

edges = []
for i in range(len(sensors) - 1):
    edges.append((sensors[i + 1] - sensors[i], i, i + 1))

edges.sort(key=lambda x: x[0], reverse=True)

cut = []
for e in edges:
    if k == 1:
        break
    k -= 1
    cut.append(e[2])
cut.sort()
cut.append(len(sensors))

total = 0
last = 0
for c in cut:
    total += sensors[c - 1] - sensors[last]
    last = c
print(total)