# 이중 우선순위 큐
from heapq import *

T = int(input())
for _ in range(T):
    k = int(input())
    minQ = []
    maxQ = []
    minQ_ignoreQ = []
    maxQ_ignoreQ = []

    for _ in range(k):
        cmd, num = input().split()
        num = int(num)
        if cmd == 'I':
            heappush(minQ, num)
            heappush(maxQ, -num)
        else:
            if num == -1 and minQ:
                d = heappop(minQ)
                heappush(maxQ_ignoreQ, -d)
            elif num == 1 and maxQ:
                d = heappop(maxQ)
                heappush(minQ_ignoreQ, -d)
        while maxQ_ignoreQ and maxQ_ignoreQ[0] == maxQ[0]:
            heappop(maxQ)
            heappop(maxQ_ignoreQ)
        while minQ_ignoreQ and minQ_ignoreQ[0] == minQ[0]:
            heappop(minQ)
            heappop(minQ_ignoreQ)
    
    if minQ:
        print(-maxQ[0], minQ[0])
    else:
        print('EMPTY')