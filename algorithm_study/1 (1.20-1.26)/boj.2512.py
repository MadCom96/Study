# 예산

n = int(input())
fund_requests = list(map(int, input().split()))
# 정해진 총액
m = int(input())


def solution() -> int:
    global n, fund_requests, m
    start = 0
    end = max(fund_requests) + 1

    while start + 1 < end:
        mid = (start + end) // 2
        if check(mid):
            start = mid
        else:
            end = mid
    return start


def check(mid: int) -> bool:
    s = 0
    for fr in fund_requests:
        s += min(fr, mid)
    if s <= m:
        return True


print(solution())

# 0, 1, 2, 3, 4, 5, 6, 7, 8| 9
# f, f, f, f, f, f, f, t, t| t
# s           v            | e
#             s     v      | e
#                   s  v   | e
#                      s  v| e
#                      s  e|
#                      v   |
#                      s  e|