# 플래피 버드 스코어링
n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
q = int(input())
w = list(map(int,input().split()))

a.append(0)
b.append(0)
ww = [[i, w[i], 0] for i in range(q)]
ww.append([-1, 0, 0])
ww.sort(key=lambda x:x[1])


lim = q + 1
for i in range(n + 1):
    width = a[i] - b[i]
    l = 0
    r = lim
    m = 0
    while l + 1 != r:
        m = (l + r) // 2
        if ww[m][1] <= width:
            l = m
        else:
            r = m
    for j in range(r, lim):
        ww[j][2] = i
    # print(width, ww)
    lim = r

ww.sort(key=lambda x:x[0])
for i in range(1, q+1):
    print(ww[i][2])