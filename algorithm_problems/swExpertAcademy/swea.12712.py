areas = [[]]

def spray(y, x, dy, dx, m):
    if 0 <= y < len(areas) and 0 <= x < len(areas) and m > 0:
        return (areas[y][x] + spray(y + dy, x + dx, dy, dx, m-1))
    else:
        return 0

test_case = int(input())
for tc in range(test_case):

    n, m = map(int, input().split())
    areas = [list(map(int, input().split())) for _ in range(n)]

    ans = 0
    for y in range(n):
        for x in range(n):
            tmp = areas[y][x]
            for dy, dx in ((0, 1), (1, 0), (-1, 0), (0, -1)):
                tmp += spray(y+dy, x+dx, dy, dx, m-1)
            if tmp > ans:
                ans = tmp

            tmp = areas[y][x]
            for dy, dx in ((-1, -1), (1, -1), (-1, 1), (1, 1)):
                tmp += spray(y+dy, x+dx, dy, dx, m-1)
            if tmp > ans:
                ans = tmp
    
    print(f'#{tc+1} {ans}')