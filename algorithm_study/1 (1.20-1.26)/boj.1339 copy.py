# 단어 수학

n = int(input())
emptyChr = '-'

lines = []
for _ in range(n):
    line = input()
    line = emptyChr * (8 - len(line)) + line
    lines.append(line)

alphaMap = {}
nextHighest = 9
for i in range(26):
    alphaMap[chr(ord('A') + i)] = -1


def getOrderedStr(l: list, i: int) -> str:
    if len(l) == 0:
        return ''
    if len(l) == 1:
        return l[0]
    if i == 8:
        ans = ''
        for ll in l:
            ans = ans + ll
        return ans
    # check 는 있는 알파벳
    # l 은 없는 알파벳
    check = []
    for line in lines:
        if line[i] in l:
            check.append(line[i])
            l.remove(line[i])
    return getOrderedStr(check, i + 1) + getOrderedStr(l, i + 1)


for i in range(8):
    alphasForIndex = []
    for line in lines:
        if line[i] != emptyChr:
            if alphaMap[line[i]] == -1:
                alphasForIndex.append(line[i])
    alphasForIndex = list(set(alphasForIndex))
    if len(alphasForIndex) == 0:
        continue
    elif len(alphasForIndex) == 1:
        alphaMap[alphasForIndex[0]] = nextHighest
        nextHighest -= 1
    else:
        s = getOrderedStr(alphasForIndex, i + 1)
        for schr in s:
            alphaMap[schr] = nextHighest
            nextHighest -= 1

def toInt(s: str) -> int:
    num = 0
    for i in range(10):
        if s[i] != emptyChr:
            s = s[i:]
            break
    for si in s:
        num *= 10
        num += alphaMap[si]
    return num

nums = []
for line in lines:
    nums.append(toInt(line))

print(sum(nums))