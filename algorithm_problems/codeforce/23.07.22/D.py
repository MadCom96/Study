for _ in range(int(input())):
    n, k = map(int, input().split())
    diff = list(map(int, input().split()))
    diff.sort()
    diff.append(diff[-1] + 10**9 + 1)
    longestGroupLength = 0
    counter = 1
    for i in range(1, n + 1):
        if diff[i] - diff[i-1] <= k:
            counter += 1
        else:
            if longestGroupLength < counter:
                longestGroupLength = counter
            counter = 1
    print(n - longestGroupLength)