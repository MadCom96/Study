# 스티커 붙이기
# 아마 미완성
n, m = 0, 0
board = []
stickers = []
s_info = []

def solution():
    global n, m, board, stickers, s_info

    # board 크기 맞춰주기
    board = [[0] * m for _ in range(n)]
    ans = 0
    
    # 스티커마다 고려
    for _ in range(len(stickers)):
        sticker = stickers.pop(0)
        r, c = s_info.pop(0)
        isok = True

        # 첫번째 모양 고려
        for y in range(n - r):
            for x in range(m - c):
                # 스티커 칸들 고려
                isok = True
                for sy in range(r):
                    for sx in range(c):
                        if board[y+sy][x+sx] == 0 or sticker[sy][sx] == 0:
                            pass
                        else:
                            isok = False
                            break
                    if not isok:
                        break
                if isok:
                    for sy in range(r):
                        for sx in range(c):
                            board[y+sy][x+sx] += sticker[sy][sx]
                            ans += sticker[sy][sx]
                    break
            if isok:
                break
        if isok:
            continue

        # 두번째 모양 고려
        for y in range(n - c):
            for x in range(m - r):
                # 스티커 칸들 고려
                isok = True
                for sy in range(r):
                    for sx in range(c):
                        if board[y + sx][x + r - sy - 1] == 0 or sticker[sy][sx] == 0:
                            pass
                        else:
                            isok = False
                            break
                    if not isok:
                        break
                if isok:
                    for sy in range(r):
                        for sx in range(c):
                            board[y + sx][x + r - sy - 1] += sticker[sy][sx]
                            ans += sticker[sy][sx]
                    break
            if isok:
                break
        if isok:
            continue

        # 세번째 모양 고려
        for y in range(n - r):
            for x in range(m - c):
                # 스티커 칸들 고려
                isok = True
                for sy in range(r):
                    for sx in range(c):
                        if board[y + r - sy - 1][x + c - sx - 1] == 0 or sticker[sy][sx] == 0:
                            pass
                        else:
                            isok = False
                            break
                    if not isok:
                        break
                if isok:
                    for sy in range(r):
                        for sx in range(c):
                            board[y + r - sy - 1][x + c - sx - 1] += sticker[sy][sx]
                            ans += sticker[sy][sx]
                    break
            if isok:
                break
        if isok:
            continue

        # 네번째 모양 고려
        for y in range(n - c):
            for x in range(m - r):
                # 스티커 칸들 고려
                isok = True
                for sy in range(r):
                    for sx in range(c):
                        if board[y + c - sx - 1][x + sy] == 0 or sticker[sy][sx] == 0:
                            pass
                        else:
                            isok = False
                            break
                    if not isok:
                        break
                if isok:
                    for sy in range(r):
                        for sx in range(c):
                            board[y + c - sx - 1][x + sy] += sticker[sy][sx]
                            ans += sticker[sy][sx]
                    break
            if isok:
                break
        if isok:
            continue
    
    return ans


def main():
    global n, m, stickers, s_info

    n, m, k = map(int, input().split())
    for _ in range(k):
        r, c = map(int, input().split())
        sticker = []
        for _ in range(r):
            sticker.append(list(map(int, input().split())))
        stickers.append(sticker)
        s_info.append((r, c))
    
    print(solution())
        

    
main()