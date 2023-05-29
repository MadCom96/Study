import sys
from heapq import *
input = sys.stdin.readline

q = []
n = int(input())
for _ in range(n):
    cmd = int(input())
    if cmd == 0:
        # print('출력')
        if q:
            print(heappop(q)[1])
        else:
            print(0)
    else:
        heappush(q, (abs(cmd), cmd))