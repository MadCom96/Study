# 강의실 배정
from heapq import * 

n = int(input())
lecture = []
for i in range(n):
    a, b = map(int, input().split())
    heappush(lecture, (a, b))

room = [0]
while lecture:
    start, end = heappop(lecture)
    finishedRoom = room[0]
    if finishedRoom <= start:
        heappop(room)
        heappush(room, end)
    else:
        heappush(room, end)

print(len(room))