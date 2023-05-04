# 교환
from collections import deque
from math import log10

n, k = map(int, input().split())
visited = set()
visited.add((n, k))

def swap(num, i, j):
    ni = num // (10**i) % 10
    nj = num // (10**j) % 10
    return num - ni*(10**i) - nj*(10**j) + ni*(10**j) + nj*(10**i)

dq = deque([(n, k)])
ans = -1
while dq:
    num, cnt = dq.popleft()

    if cnt == 0:
        if num > ans:
            ans = num
        continue

    length = int(log10(num)) + 1
    for i in range(length-1):
        for j in range(i+1, length):
            nextnum = swap(num, i, j)
            if int(log10(nextnum))+1 != length:
                continue
            if (nextnum, cnt-1) in visited:
                continue
            dq.append((nextnum, cnt-1))
            visited.add((nextnum, cnt-1))
print(ans)