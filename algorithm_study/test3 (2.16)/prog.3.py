# 코딩 테스트 공부
from collections import deque

ways = [[0, 0, 1, 0, 1], [0, 0, 0, 1, 1]]
inf = 301
dp = [[inf] * 151 for _ in range(151)]

def solution(alp, cop, problems):
    answer = 0


    al_goal = 0
    co_goal = 0
    for p in problems:
        if p[0] > al_goal:
            al_goal = p[0]
        if p[1] > co_goal:
            co_goal = p[1]
    
    # 나의 상태를 알고력, 코딩력, 시간으로 표시
    now = [alp, cop]
    bfs = deque([now])
    dp[alp][cop] = 0
    while len(bfs) != 0:
        now = bfs.popleft()
        # 가능한 문제를 제거하고 길에 추가
        i = 0
        while True:
            if i < len(problems):
                if problems[i][0] <= now[0] and problems[i][1] <= now[1]:
                    ways.append(problems.pop(i))
                    i -= 1
                i += 1
            else:
                break
                
        for way in ways:
            if alp <= now[0]+way[2] <= al_goal and cop <= now[1]+way[3] <= co_goal:
                dp[now[0]+way[2]][now[1]+way[3]] = min(dp[now[0]+way[2]][now[1]+way[3]], dp[now[0]][now[1]] + way[4])
                bfs.append([now[0]+way[2], now[1]+way[3]])

    return dp[alp][cop]


# 문제의 정보들
# [alp_req, cop_req, alp_rwd, cop_rwd, cost]
# 최대 100개

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