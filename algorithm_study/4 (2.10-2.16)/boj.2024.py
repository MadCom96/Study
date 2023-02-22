import sys
from collections import deque

input = sys.stdin.readline

n = int(input())

lines = []
while True:
    start, end = map(int, input().split())
    if start == 0 and end == 0:
        break

    if start == end: 
        continue

    if start < 0 and end <= 0:
        continue

    lines.append((start, end))

sorted_lines = deque(sorted(lines))


def solution():
    index = 0 
    cnt = 0

    while sorted_lines:
        possibles = []

        now_line = sorted_lines.popleft()
        if now_line[0] <= index: 
            possibles.append(now_line[1])

        if index < now_line[0]:  
            return 0

        while sorted_lines:
            tmp = sorted_lines.popleft()

            if tmp[0] <= index:
                possibles.append(tmp[1])
            else:
                sorted_lines.appendleft(tmp)
                break

        index = max(possibles)
        cnt += 1

        if index >= n:
            return cnt

    return 0


print(solution())


# 대체 뭐가 다른건지 진짜로 모르겠다....