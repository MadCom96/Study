T = 0
E = 0
CHARGE = []
DIST = []
comb = []
ans = []

def simulation():
    global T, E, CHARGE, DIST, comb, ans
    time = 0
    energy = 0
    if comb[:3] == [3, 1, 3]:
        print()
    for i in range(len(comb)):
        n = comb[i]
        time += n
        energy += n * CHARGE[i]

        if energy + time // T * E == 0:
            return

        d = DIST[i]
        time += d
        energy -= d
        if energy + time // T * E < 0:
            return
        if time > ans[0]:
            return
        elif time == ans[0] and energy + time // T * E < ans[1]:
            return
    ans = [time, energy + time // T * E]

    print('comb:', comb)
    print('ans:',ans)
    print()


def dfs(ith):
    global T, E, CHARGE, DIST, comb

    if ith == len(comb):
        simulation()
        return

    n = 0
    while n * CHARGE[ith] <= sum(DIST[ith:]):
        comb[ith] = n
        dfs(ith + 1)
        n += 1


def solution(t, e, charge, dist):
    global T, E, CHARGE, DIST, comb, ans
    T = t
    E = e
    CHARGE = charge
    DIST = dist
    comb = [0] * len(dist)
    ans = [1e12 + 1, 1e12 + 1]

    dfs(0)
    return ans


print(solution(
    3, 1, 
    [1, 2, 3, 4, 1],
    [4, 4, 7, 9]
))
# [31, 3]
print()

print(solution(
    1, 1,
    [3, 10, 10, 10],
    [3, 14, 30]
))
# [48, 4]
print()