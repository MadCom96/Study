# 코딩 테스트 공부
from collections import deque

dp = []

def solution(alp, cop, problems):
    global dp

    al_goal = 0
    co_goal = 0
    for p in problems:
        if p[0] > al_goal:
            al_goal = p[0]
        if p[1] > co_goal:
            co_goal = p[1]

    dp = [[ (i - alp) + (j - cop) for j in range(151)] for i in range(151)]

    problems.sort(key=lambda x: (x[0]+x[1]))

    for p in problems:
        for i in range(p[0], 150 - p[2]):
            for j in range(p[1], 150 - p[3]):
                dp[i+p[2]][j+p[3]] = min(dp[i+p[2]][j+p[3]], dp[i][j] + p[4])
    
    return dp[al_goal][co_goal]
   

if __name__ == "__main__":
    print(solution(10, 10, [
        [10,15,2,1,2],
        [20,20,3,3,4]
    ]))
    print(solution(0, 0, [
        [0,0,2,1,2],
        [4,5,3,1,2],
        [4,11,4,0,2],
        [10,4,0,4,2]
    ]))