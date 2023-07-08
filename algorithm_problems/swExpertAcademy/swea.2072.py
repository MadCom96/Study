t = int(input())

for i in range(t):
    arr = list(map(int, input().split()))
    total = 0
    for a in arr:
        if a % 2 == 1:
            total += a
    print(f'#{i+1} {total}')