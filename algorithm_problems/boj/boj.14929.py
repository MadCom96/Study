n = int(input())
xi = list(map(int, input().split()))
sums = [0] * n

total = 0
for i in range(n):
    total += xi[i]
    sums[i] = total

ans = 0
for i in range(n-1):
    ans += xi[i] * (sums[-1] - sums[i])
print(ans)