dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]
dirnum = {'U':0, 'D':1, 'R':2, 'L':3}

movedset = set()

def solution(dirs):
    answer = 0
    
    now = [0, 0]
    for dir in dirs:
        nextloc = now[:]
        dn = dirnum[dir]

        # 유효한 move인가 체크
        nextloc[0] += dy[dn]
        nextloc[1] += dx[dn]
        if not (-5<=nextloc[0]<=5 and -5<=nextloc[1]<=5):
            continue
        
        # 움직인적 있는지 체크
        move1 = (now[0], now[1], nextloc[0], nextloc[1])
        if not (move1 in movedset):
            answer += 1
            move2 = (nextloc[0], nextloc[1], now[0], now[1])
            movedset.add(move1)
            movedset.add(move2)
        
        now = nextloc
    return answer

#=======================================
dirs = input()
print(solution(dirs))