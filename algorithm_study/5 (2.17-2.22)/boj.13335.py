# 트럭
from collections import deque

n, w, L = map(int, input().split())
trucks = deque(map(int, input().split()))

bridge = deque([0] * w)
totalW = 0

time = w
while trucks:
    time += 1
    totalW -= bridge[0]
    bridge.popleft()

    if len(trucks) > 0 and totalW + trucks[0] <= L:
        totalW += trucks[0]
        bridge.append(trucks.popleft())
    else:
        bridge.append(0)

print(time)