# 줄임말

s = input()
t = input()

count = 1
lastTindex = -1

tIndex = [[] for i in range(26)]
tII = [0 for i in range(26)]


def getI(alpha: str) -> int:
    return ord(alpha) - ord('a')


def check(a) -> bool:
    if len(tIndex[a]) == tII[a]:
        return False
    l = tII[a]-1
    r = len(tIndex[a]) - 1
    while l != r - 1:
        m = (l + r) // 2
        m += (l + r) % 2
        if tIndex[a][m] < lastTindex:
            l = m
        else:
            r = m

    if tIndex[a][r] > lastTindex:
        tII[a] = r
        return True
    else:
        return False


for i in range(len(t)):
    tIndex[getI(t[i])].append(i)

i = 0
while i < len(s):
    # a 현재 다루는 s 알파벳의 인덱스
    a = getI(s[i])

    if len(tIndex[a]) == 0:
        count = -1
        break

    if check(a):
        lastTindex = tIndex[a][tII[a]]
        tII[a] += 1
        i += 1
    else:
        count += 1
        tII = [0 for i in range(26)]
        lastTindex = -1
print(count)
