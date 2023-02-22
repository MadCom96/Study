# 흩날리는 시험지 속에서 내 평점이 느껴진거야
# 공유기 설치 문제와 유사했다.
n, k = map(int, input().split())
x = list(map(int, input().split()))
sums = [0]
for xx in x:
    sums.append(sums[-1] + xx)
sums.pop(0)

def upperbound(i):
    global n, k, sums
    l = 0
    r = n
    while l != r:
        m = (l+r) // 2
        if sums[m] == i:
            return m
        elif sums[m] < i:
            l = m + 1
        else:
            r = m
    return r

def check(m):
    global n, k, sums
    cnt = 0
    i = m
    while True:
        next_idx = upperbound(i)
        if next_idx == n:
            return False
        cnt += 1
        if cnt >= k:
            return True
        i = sums[next_idx] + m

l = 0
r = 10 ** 5 * 20 + 1
while l + 1 != r:
    m = (l + r) // 2
    if check(m):
        l = m
    else:
        r = m
print(l)