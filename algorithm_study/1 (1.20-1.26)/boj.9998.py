# 블록 쌓기
n = int(input())
y = list(map(int,input().split()))
d = list(map(int,input().split()))

def check(cc):
    midC = n // 2
    total = 0
    for i in range(n):
        total += abs(abs(midC - i) + cc - y[i])
        total += abs(abs(midC - i) + cc - d[i])
    return total

# 진짜 어이없는게 최대블럭수 고려안해줬다고 틀렸다
# 그걸 고려 안한 내가 어이가 없다는 뜻
l = 0
r = 10**12 - n//2
m = 0
while l + 1 != r:
    m = (l + r) // 2
    if check(l) < check(r):
        r = m
    else:
        l = m
print(min(check(l), check(r)))