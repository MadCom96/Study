sudoku = []

def cellTest33() -> bool:
    global sudoku
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            counter = set()
            for y in range(i, i+3):
                for x in range(j, j+3):
                    counter.add(sudoku[y][x])
            if len(counter) != 9:
                return False
    return True

def verhortest() -> bool:
    global sudoku
    for y in range(9):
        counter = set()
        for x in range(9):
            counter.add(sudoku[y][x])
        if len(counter) != 9:
            return False

    for x in range(9):
        counter = set()
        for y in range(9):
            counter.add(sudoku[y][x])
        if len(counter) != 9:
            return False
    
    return True


test_case = int(input())
for tc in range(test_case):
    sudoku = [list(map(int, input().split())) for _ in range(9)]
    if cellTest33() and verhortest():
        print(f'#{tc+1} 1')
    else:
        print(f'#{tc+1} 0')