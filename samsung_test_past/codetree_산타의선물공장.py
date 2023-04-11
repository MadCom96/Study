from collections import deque

q = int(input())

m = 0
belts = []
idSets = []
belts_malfunctioning = set()

def fac_foundation(data: list) -> None:
    global m, belts, idSets, belts_malfunctioning
    n = data.pop(0)
    m = data.pop(0)
    ids = data[:n]
    weights = data[n:]
    belts.append(deque)
    idSets.append(set())

    amount = n // m
    cnt = 0
    tmpL = deque()
    tmpS = set()
    for i in range(n):
        tmpL.append((ids[i], weights[i]))
        tmpS.add(ids[i])
        cnt += 1
        if cnt == amount:
            belts.append(tmpL)
            idSets.append(tmpS)
            tmpL = deque()
            tmpS = set()
            cnt = 0


# 하차된 상자 무게의 총 합 반환
def box_withdraw(data) -> int:
    global m, belts, idSets, belts_malfunctioning 
    w_max = data[0]
    ans = 0
    for i in range(1, m + 1):
        if i in belts_malfunctioning:
            continue
        if len(belts[i]) == 0:
            continue
        box = belts[i].popleft()
        if box[1] <= w_max:
            ans += box[1]
            idSets[i].remove(box[0])
        else:
            belts[i].append(box)
    return ans


# 있다면 r_id, 없다면 -1
def box_remove(data) -> int:
    global m, belts, idSets, belts_malfunctioning
    r_id = data[0]
    for bi in range(1, m + 1):
        if bi in belts_malfunctioning:
            continue
        if r_id in idSets[bi]:
            idSets[bi].remove(r_id)        
            tmp = deque()
            while belts[bi]:
                if belts[bi][0][0] == r_id:
                    belts[bi].popleft()
                    tmp.extend(belts[bi])
                    break
                tmp.append(belts[bi].popleft())
            belts[bi] = tmp
            return r_id
    return -1
        

# 해당 박스가 있는 벨트 반환, 없다면 -1
def box_check(data) -> int:
    global m, belts, idSets, belts_malfunctioning
    f_id = data[0]
    for bi in range(1, m + 1):
        if bi in belts_malfunctioning:
            continue
        if f_id in idSets[bi]:
            tmp = deque()
            while belts[bi]:
                if belts[bi][0][0] == f_id:
                    belts[bi].extend(tmp)
                    break
                tmp.append(belts[bi].popleft())
            return bi
    return -1



# 명령 수행 전 이미 망가졌다면 -1, 아니라면 b_num
def belt_malfunction(data) -> int:
    global m, belts, idSets, belts_malfunctioning
    b_num = data[0]
    if b_num in belts_malfunctioning:
        return -1
    for i in range(1, m):
        belt_checking = (b_num - 1 + i) % m + 1
        if belt_checking in belts_malfunctioning:
            continue
        belts[belt_checking].extend(belts[b_num])
        belts[b_num] = []
        idSets[belt_checking] = idSets[belt_checking] | idSets[b_num]
        idSets[b_num].clear()
        belts_malfunctioning.add(b_num)
        return b_num

for _ in range(q):
    command = list(map(int, input().split()))
    command, data = command[0], command[1:]
    if command == 100:
        fac_foundation(data)
    elif command == 200:
        print(box_withdraw(data))
    elif command == 300:
        print(box_remove(data))
    elif command == 400:
        print(box_check(data))
    elif command == 500:
        print(belt_malfunction(data))

# https://pydole.tistory.com/80
# 2 시간 못 풀었음