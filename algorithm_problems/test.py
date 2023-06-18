def solution(queue1, queue2):
    length = len(queue1)
    total = sum(queue1) + sum(queue2)
    halftotal = total // 2
    
    mergedQ = queue1 + queue2
    # l ~ r-1
    l, r = 0, length
    partSum = sum(mergedQ[l:r])
    cnt1 = 0
    while l < length and r < 2*length:
        if partSum < halftotal:
            r += 1
            partSum += mergedQ[r-1]
            cnt1 += 1
        elif partSum > halftotal:
            l += 1
            partSum -= mergedQ[l-1]
            cnt1 += 1
        else:
            break
    if l == length or r == 2*length:
        cnt1 = -1
    
    mergedQ = queue2 + queue1
    l, r = 0, length
    partSum = sum(mergedQ[l:r])
    cnt2 = 0
    while l < length and r < 2*length:
        if partSum < halftotal:
            r+=1
            partSum += mergedQ[r-1]
            cnt2 += 1
        elif partSum > halftotal:
            l += 1
            partSum -= mergedQ[l-1]
            cnt2 += 1
        else:
            break
    if l == length or r == 2*length:
        cnt2 = -1
    
    if cnt1 == -1 and cnt2 == -1:
        return -1
    elif cnt1 == -1:
        return cnt2
    elif cnt2 == -1:
        return cnt1
    else:
        return min(cnt1, cnt2)

# 3 2 7 2 4 6 5 1 3 2 7 2 4 6 5 1
queue1 = [3, 2, 7, 2]
queue2 = [4, 6, 5, 1]
print(solution(queue1,queue2))

queue1 = [1, 2, 1, 2]
queue2 = [1, 10, 1, 2]	
print(solution(queue1,queue2))

queue1 = [3, 2, 7, 2]
queue2 = [4, 6, 5, 1]
print(solution(queue1,queue2))