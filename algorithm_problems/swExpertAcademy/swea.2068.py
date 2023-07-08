t = int(input())

for i in range(t):
    arr = list(map(int, input().split()))
    highest = 0
    for a in arr:
        if highest < a:
            highest = a
    print(f'#{i+1} {highest}')