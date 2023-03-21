# 격자 숫자 놀이
r, c, k = map(int, input().split())

cells = [list(map(int, input().split())) for _ in range(3)]
cells_next = []

def calc():
    global r, c, k, cells, cell_next
    cells_next = []
    
    column = len(cells)
    row = len(cells[0])

    column_after = column
    row_after = row

    if column >= row:
        for ci in range(column):
            cell_line = {}
            cell_set = set()
            for ri in range(row):
                if cells[ci][ri] == 0:
                    continue
                before = len(cell_set)
                cell_set.add(cells[ci][ri])
                after = len(cell_set)
                if before != after:
                    cell_line[cells[ci][ri]] = 1
                else:
                    cell_line[cells[ci][ri]] += 1
            cell_next = []
            for key, value in cell_line.items():
                cell_next.append([key, value])
            cell_next.sort(key= lambda x: (x[1], x[0]))
            cell_line = []
            for cn in cell_next:
                cell_line.append(cn[0])
                cell_line.append(cn[1])
                if len(cell_line) == 100:
                    break
            row_after = max(row_after, len(cell_line))
            cells_next.append(cell_line)
        
        cells = [[0] * row_after for _ in range(column_after)]
        for ci in range(column_after):
            for ri in range(len(cells_next[ci])):
                cells[ci][ri] = cells_next[ci][ri]

    else:
        for ri in range(row):
            cell_line = {}
            cell_set = set()
            for ci in range(column):
                if cells[ci][ri] == 0:
                    continue
                before = len(cell_set)
                cell_set.add(cells[ci][ri])
                after = len(cell_set)
                if before != after:
                    cell_line[cells[ci][ri]] = 1
                else:
                    cell_line[cells[ci][ri]] += 1
            cell_next = []
            for key, value in cell_line.items():
                cell_next.append([key, value])
            cell_next.sort(key= lambda x: (x[1], x[0]))
            cell_line = []
            for cn in cell_next:
                cell_line.append(cn[0])
                cell_line.append(cn[1])
                if len(cell_line) == 100:
                    break
            column_after = max(column_after, len(cell_line))
            cells_next.append(cell_line)

        cells = [[0] * row_after for _ in range(column_after)]
        # 이거 ri일수도 있다
        for ri in range(row_after):
            for ci in range(len(cells_next[ri])):
                cells[ci][ri] = cells_next[ri][ci]

ans = -1
for time in range(101):
    if r <= len(cells) and c <= len(cells[0]):
        if cells[r - 1][c - 1] == k:
            ans = time
            break
    calc()
print(ans)
