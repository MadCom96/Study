mat = []
converted = []

def conv90(n):
    global mat, converted
    i = 0
    for x in range(n):
        line = []
        for y in range(n-1, -1, -1):
            line.append(mat[y][x])
        converted[i].append(line[:])
        i += 1


def conv180(n):
    global mat, converted
    i = 0
    for y in range(n-1, -1, -1):
        line = []
        for x in range(n-1, -1, -1):
            line.append(mat[y][x])
        converted[i].append(line[:])
        i += 1

def conv270(n):
    global mat, converted
    i = 0
    for x in range(n-1, -1, -1):
        line = []
        for y in range(n):
            line.append(mat[y][x])
        converted[i].append(line[:])
        i += 1

def display(tc):
    global converted
    print(f'#{tc+1}')
    for c in converted:
        for sep in c:
            for letter in sep:
                print(letter, end='')
            print(' ', end='')
        print()

test_case = int(input())
for tc in range(test_case):
    n = int(input())
    mat = [list(map(int, input().split())) for _ in range(n)]
    converted = [[] for _ in range(n)]
    conv90(n)
    conv180(n)
    conv270(n)
    display(tc)