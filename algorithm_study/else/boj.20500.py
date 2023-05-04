# Ezreal 여눈부터 가네 ㅈㅈ
limit = 1000000007

comb = [[0]* 1516 for _ in range(1516)]
for n in range(1516):
    comb[n][0] = 1
    comb[n][1] = n
    for r in range(2, n // 2 + 1):
        comb[n][r] = comb[n][r-1] * (n - (r - 1)) // r 
        # comb[n][r] %= limit

def getC(n, r):
    if r > n // 2:
        r = n - r
    return comb[n][r]

n = int(input())
ans = 0
for i in range(n):
    # 끝자리는 5로 고정하고 나머지 자리수를 바꿔준다
    num5 = i
    num1 = n-1-i
    # 3의 배수라면
    if (num1 + (num5+1)*5) % 3 == 0:
        ans += getC(n-1, num5)
        ans %= limit
print(ans)