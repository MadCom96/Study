# 모자이크
import sys

column, row = map(int, input().split())
paper = int(input())
wrong = int(input())
wrong_cells = [tuple(map(int, sys.stdin.readline().rstrip().split())) for _ in range(wrong)]
wrong_cells.sort(key= lambda x:x[1])

def upperbound(i):
    l = 0
    r = wrong
    while l != r:
        m = (l + r) // 2
        if i <= wrong_cells[m][1]:
            r = m
        else:
            l = m + 1
    return l


def check(m) -> int:
    cnt = 0
    idx = 0
    while True:
        if idx >= wrong:
            break
        cnt += 1
        idx = upperbound(wrong_cells[idx][1] + m)
    return cnt


l = 1
for c in wrong_cells:
    if c[0] > l:
        l = c[0]
l -= 1
r = max(column, row)

while l + 1 != r:
    # m 색종이의 크기
    m = (l + r) // 2
    wrong_cells_copy = wrong_cells[:]
    least_paper_need = check(m)
    # mid가 조건을 만족하면 
    if least_paper_need <= paper:
        r = m
    else:
        l = m

print(r)