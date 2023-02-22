# 감시
from copy import deepcopy

n, m = map(int, input().split())
office = [list(map(int, input().split())) for _ in range(n)]

# 동 남 서 북
dir = [(0, 1), (1, 0), (0, -1), (-1, 0)]
cctv = [
    [],
    [((dir[0]), ), ((dir[1]), ), ((dir[2]), ), ((dir[3]), )],
    [(dir[0], dir[2]), (dir[1], dir[3])],
    [(dir[0], dir[1]), (dir[0], dir[3]),
    (dir[1], dir[2]), (dir[2], dir[3])],
    [(dir[0], dir[1], dir[2]), (dir[0], dir[1], dir[3]), (dir[0], dir[2], dir[3]), (dir[1], dir[2], dir[3])],
    [tuple(dir)]
]
# cctv[번호][포지션번호] -> n대의 카메라
# cctv[번호][포지션번호][카메라번호] -> (y좌표, x좌표)

# [y, x, 카메라번호, 포지션]
cctv_info = []
min_space = 0
for i in range(n):
    for j in range(m):
        if office[i][j] == 0:
            min_space += 1
        elif office[i][j] == 6:
            pass
        else:
            cctv_info.append([i, j, office[i][j], 0])

def simul():
    global n, m, office, cctv, cctv_info
    tmp = deepcopy(office)
    for ith_cctv in cctv_info:
        y = ith_cctv[0]
        x = ith_cctv[1]
        cam_num = ith_cctv[2]
        cam_pos = ith_cctv[3]
        for c in cctv[cam_num][cam_pos]:
            for i in range(8):
                if 0 <= y + c[0] * i < n and 0 <= x + c[1] * i < m:
                    if tmp[y + c[0] * i][x + c[1] * i] == 6:
                        break
                    elif tmp[y + c[0] * i][x + c[1] * i] == 0:
                        tmp[y + c[0] * i][x + c[1] * i] = 7
                else:
                    break
    ans = 0
    for officeLine in tmp:
        ans += officeLine.count(0)
    return ans

def dfs(ith):
    global n, m, office, cctv, cctv_info, min_space
    pos = len(cctv[cctv_info[ith][2]])
    for i in range(pos):
        cctv_info[ith][3] = i
        if ith == len(cctv_info) - 1:
            min_space = min(simul(), min_space)
        else:
            dfs(ith + 1)

# if 없으면 cctv가 하나도 없는 경우에도 하나는 있다고 가정하고 풀어 index error발생
if cctv_info:
    dfs(0)
print(min_space)