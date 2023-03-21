# 놀이 공원
n, m = map(int, input().split())
rides = list(map(int, input().split()))

if n <= m:
    print(n)
    exit()

l = 0
r = 2000000000 * 30 + 1
children = 0
while l + 1 != r:
    mid = (l+r)//2
    children = m + 1
    for ride in rides:
        children += mid // ride
    if children > n:
        r = mid
    else:
        l = mid
print(l)
children = m
for ride in rides:
    children += l // ride
print(children)

while True:
    l += 1
    for ri in range(m):
        if l % rides[ri] == 0:
            children += 1
            if children == n:
                print(ri + 1)
                exit()