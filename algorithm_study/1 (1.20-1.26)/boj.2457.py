# 공주님의 정원
n = int(input())

flowers = []
for i in range(n):
    flowers.append(tuple(map(int, input().split())))

# 끝나는 날짜도 고려하여 sort
flowers.sort(key= lambda x : (x[0], x[1], x[2], x[3]))
flowers.append((13, 0, 0, 0))

# 1 이 2보다 같거나 빠르면 트루
# 2 가 1보다 같거나 느리면 트루
def earlier(m1, d1, m2, d2) -> bool:
    if m1 < m2:
        return True
    elif m1 == m2:
        if d1 <= d2:
            return True
        else:
            return False
    else:
        return False


# 커버해야되는 최소날짜
startDay = (3, 1) 
lastDayCanBeCovered = (0, 0)
considering = 0
count = 0
i = 0
connected = False
while i < n + 1:
    sm, sd, em, ed = flowers[i]
    if earlier(sm, sd, startDay[0], startDay[1]):
        connected = True
        if not earlier(em, ed, lastDayCanBeCovered[0], lastDayCanBeCovered[1]):
            lastDayCanBeCovered = (em, ed)
            considering = i
        i += 1
    else:
        count += 1
        if earlier(12, 1, lastDayCanBeCovered[0], lastDayCanBeCovered[1]):
            break
        if not connected:
            count -= 1
            break
        connected = False
        startDay = lastDayCanBeCovered

if earlier(lastDayCanBeCovered[0], lastDayCanBeCovered[1], 11, 30):
    count = 0
print(count)

