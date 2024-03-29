# 줄임말
s = input()
t = input()

count = 1
lastTindex = -1

tIndex = [[] for i in range(26)]
tII = [0 for i in range(26)]


def getI(alpha: str) -> int:
    return ord(alpha) - ord('a')

# 현재 T에서 덧붙히지 않고 해당 알파벳을 찾을 수 있는가?
def check(a) -> bool:
    if len(tIndex[a]) == tII[a]:
        return False
    # 역 매개변수 이분탐색
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
    # 만약 현재 알파벳이 t에 없으면
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