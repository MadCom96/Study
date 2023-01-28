# 먹을 것인가 먹힐 것인가.
import sys
input = sys.stdin.readline

TC = int(input())
for _ in range(TC):
    n, m = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    B.append(0) # 조건에 없는 무조건 되는 경우를 [0]에 넣기 위함
    B.sort()

    lB = len(B)
    ans = 0
    for a in A:
        left = 0
        right = lB
        while left + 1 < right:
            mid = (left + right) // 2
            if B[mid] < a:
                left = mid
            else:
                right = mid
        ans += left
    print(ans)