dg = []
route = []
best = 0
isin = [False]

# k = 현재 남은 피로도
def rec(k):
    global dg, route, best, isin
    
    for i in range(len(isin)):
        if (not isin[i]) and dg[i][0] <= k:
            isin[i] = True
            route.append(i)
            rec(k - dg[i][1])
            route.pop()
            isin[i] = False
    if best < len(route):
        best = len(route)

# k = 피로도
# [최소 필요 피로도, 소모 피로도]
def solution(k, dungeons):
    global dg, best, isin
    dg = dungeons
    best = 0
    isin = [False] * len(dungeons)
    rec(k)
    return best
    

if __name__ == "__main__":
    k = 80
    dungeons = [[80,20],[50,40],[30,10]]
    print(solution(k, dungeons))

    k = 10
    dungeons = [[80,20],[50,40],[30,10]]
    print(solution(k, dungeons))