# 개표
import sys
input = sys.stdin.readline
n, q = map(int, input().rstrip().split())

# 다른 사람들의 합
sumOthers = 0
# 다른 사람들 중 highest
highestOthers = 0
# 다른 사람 hightest를 구하기 위해 배열 사용. 나 포함
votes = [0 for i in range(n + 2)]

for i in range(q):
    cmd, x, y = map(int, input().rstrip().split())

    if cmd == 1:
        votes[y] += x
        #다른 사람일 경우
        if y != n + 1:
            sumOthers += x
            if votes[y] > highestOthers:
                highestOthers = votes[y]
    else:
        if votes[-1] + x > highestOthers:
            if (votes[-1] + x - 1) * n  < sumOthers + y: 
                print("NO")
            else:
                print("YES")
        else:
            print("NO")