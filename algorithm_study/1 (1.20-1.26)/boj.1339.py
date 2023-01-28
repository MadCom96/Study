# 단어 수학
# 진짜 멍청하게 풀었다...
n = int(input())
linesReversed = []
alphaHave = set()
for _ in range(n):
    line = input()
    for s in line:
        alphaHave.add(s)
    linesReversed.append(line[::-1])

alphaHave = list(alphaHave)
counts = {}
for a in alphaHave:
    counts[a] = 0

for i in range(8):
    for line in linesReversed:
        if len(line) > i:
            counts[line[i]] += 10 ** i

cs = []
for v in counts.values():
    cs.append(v)
cs.sort(reverse=True)

total = 0
nextHightest = 9
for c in cs:
    total += nextHightest * c
    nextHightest -= 1
print(total)