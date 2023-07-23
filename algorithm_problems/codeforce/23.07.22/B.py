t = int(input())
while t:
    t -= 1
    n = int(input())
    highest = -1
    hidx = -1
    for i in range(1, 1 + n):
        a, b = map(int, input().split())
        if a <= 10 and b > highest:
            highest = b
            hidx = i
    print(hidx)
