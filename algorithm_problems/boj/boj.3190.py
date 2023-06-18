# 뱀
n, k = 0, 0
l = 0
moves = []
field = []

# 시계. 동 남 서 북
dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

def getInput():
    global n, k, l, moves, field

    n = int(input())
    k = int(input())
    field = [[0] * (n) for _ in range(n)]
    for _ in range(k):
        r, c = map(int, input().split())
        field[r-1][c-1] = 2

    l = int(input())
    for _ in range(l):
        r, c = input().split()
        moves.append((int(r), c))

def solution():
    global n, k, l, moves, dy, dx
    snake = [(0, 0)]
    field[0][0] = 1
    sd = 0

    time = -1
    while True:
        time += 1
        if moves and moves[0][0] == time:
            _, direction = moves.pop(0)
            if direction == 'D':
                sd = (sd+1) % 4
            else:
                sd = (sd-1) % 4

        y, x = snake[0]
        yy = dy[sd] + y
        xx = dx[sd] + x

        if not (0<=yy<n and 0<=xx<n):
            break
        elif field[yy][xx] == 1:
            break
        elif field[yy][xx] == 2:
            snake.insert(0, (yy, xx))
            field[yy][xx] = 1
        else:
            snake.insert(0, (yy, xx))
            field[yy][xx] = 1
            taily, tailx = snake.pop()
            field[taily][tailx] = 0
        
    return time + 1

if __name__ == "__main__":
    getInput()
    print(solution())