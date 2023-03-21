# 순회강연
n = int(input())
q = []
for _ in range(n):
    p, d = map(int, input().split())
    q.append((p, d))

q.sort(key=lambda x : (-x[0], -x[1]))

days = [False] * 10001

ans = 0
while q:
    lec = q.pop(0)
    for i in range(lec[1], 0, -1):
        if not days[i]:
            ans += lec[0]
            days[i] = True
            break

print(ans)