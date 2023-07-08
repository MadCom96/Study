test_case = int(input())
for tc in range(test_case):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    # b를 항상 큰 쪽으로 고정
    if n > m:
        a, b = b, a
        n, m = m, n
    
    ans = 0
    for i in range(n):
        ans += a[i] * b[i]

    for offset in range(1, m - n + 1):
        tmp = 0
        for i in range(n):
            tmp += a[i] * b[offset + i]
        ans = max(tmp, ans)
    
    print(f'#{tc+1} {ans}')