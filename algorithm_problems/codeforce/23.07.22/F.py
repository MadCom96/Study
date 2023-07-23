from collections import defaultdict

# 최적화 필요할 것 같음
t = int(input())

counter = []

for _ in range(t):
    n = int(input())
    counter = [0] * (n + 1)
    hops = list(map(int, input().split()))
    hopdict = defaultdict(int)
    for hop in hops:
        hopdict[hop] += 1

    hopset = set(hopdict.keys())
    ans = 0

    while hopset:
        hop = hopset.pop()
        i = 1
        while hop * i <= n:
            counter[hop * i] += hopdict[hop]
            if ans < counter[hop * i]:
                ans = counter[hop * i]
            i += 1
    [hop * i]
    print(ans)