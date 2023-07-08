T = int(input())

def solution(x1, y1, r1, x2, y2, r2):
    if x1 == x2 and y1 == y2:
        if r1 == r2:
            return -1
        else:
            return 0

    distSquare = (x1-x2) ** 2 + (y1-y2) ** 2
    dist = distSquare ** 0.5

    if dist > r1 and dist > r2:
        if r1 + r2 == dist:
            return 1
        elif r1 + r2 > dist:
            return 2
        else:
            return 0
    else:
        


    

for _ in range(T):
    print(solution(*tuple(map(int, input().split()))))