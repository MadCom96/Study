# 공유기 설치
import sys
input = sys.stdin.readline

n, c = map(int, input().rstrip().split())
x = [int(input().rstrip()) for _ in range(n)]
x.sort()

# 인덱스로 반환
# 다음 인덱스를 찾는 upperbound 이분탐색
def upper_bound(i) -> int:
    global n, c, x
    l = 0
    r = n
    while l != r:
        m = (l + r) // 2
        if x[m] == i:
            return m
        elif x[m] < i:
            l = m + 1
        elif x[m] > i:
            r = m
    return r


def check(m) -> bool:
    global n, c, x
    cnt = 0
    i = 0
    while True:
        next_spot_idx = upper_bound(i)
        cnt += 1
        if cnt >=  c:
            return True
        i = x[next_spot_idx] + m
        if i > x[-1]:
            return False


# 매개변수 이분탐색
l = 1
r = x[-1] + 1
while l + 1 != r:
    m = (l + r) // 2
    if check(m):
        l = m
    else:
        r = m
print(l)