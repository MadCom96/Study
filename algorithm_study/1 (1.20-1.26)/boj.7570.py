# 줄 세우기
n = int(input())
kids = list(map(int, input().split()))

kidLoc = [0 for _ in range(len(kids) + 1)]
for i in range(n):
    kidLoc[kids[i]] = i + 1

# 범위 전체는 n + 1, 마지막 원소 검사x (n+1)-1
longestLine = 0
temp = 0
for i in range(1, n):
    if kidLoc[i] < kidLoc[i+1]:
        temp += 1
    else:
        if longestLine < temp:
            longestLine = temp
        temp = 0

print(n - longestLine - 1)