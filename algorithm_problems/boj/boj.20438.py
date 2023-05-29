import sys
input = sys.stdin.readline

n, k, q, m = map(int, input().split())

sleepers = list(map(int, input().split()))
who_sleeps = [False] * (n+3)
for s in sleepers:
    who_sleeps[s] = True

coders = list(map(int, input().split()))
who_coded = [False] * (n+3)
for c in coders:
    who_coded[c] = True

checked = [False] * (n+3)
cnt = 0

for i in range(3, n+3):
    if who_sleeps[i]:
        who_coded[i] = False
    if who_coded[i]:
        for wc in range(i, n+3, i):
            who_coded[wc] = True

cumulative_sum = [0] * (n*3)

for i in range(3, n+3):
    cumulative_sum[i] = cumulative_sum[i-1]
    if not who_coded[i]:
        cumulative_sum[i] += 1

for _ in range(m):
    l, r = map(int, input().split())
    print(cumulative_sum[r] - cumulative_sum[l-1])