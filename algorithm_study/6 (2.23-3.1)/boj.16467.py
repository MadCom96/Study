# 병아리의 변신은 무죄
import sys
input = sys.stdin.readline

class Matrix:
    def __init__(self, l: list = []) -> None:
        self.m = l

    def getKM(self, k):
        if k == 0:
            self.m = [[2]]
            return
        self.m = [[0] * (k + 1) for _ in range(k + 1)]
        self.m[0][0] = 1
        self.m[0][-1] = 1
        for i in range(1, k + 1):
            self.m[i][i - 1] = 1
    
    def getZeros(self, y, x):
        self.m = [[0] * x for _ in range(y)]
    
    def getEyes(self, k):
        self.getZeros(k, k)
        for i in range(k):
            self.m[i][i] = 1

    def __mul__(self, mat):
        if len(self.m[0]) != len(mat.m):
            exit(-1)
        tmp = Matrix()
        tmp.getZeros(len(self.m), len(mat.m[0]))
        for y in range(len(tmp.m)):
            for x in range(len(tmp.m[0])):
                for k in range(len(self.m[0])):
                    tmp.m[y][x] += self.m[y][k] * mat.m[k][x]
                    # 없으면 시간초과
                    tmp.m[y][x] = int(tmp.m[y][x] % 100000007)
        return tmp

def power(M: Matrix, k: int) -> Matrix:
    R = Matrix()
    if k == 0:
        R.getEyes(len(M.m))
    if k == 1:
        return M
    R = power(M, k // 2)
    R = R * R
    if k % 2 == 1:
        R = R * M
    return R

m = Matrix()
m_orig = Matrix()


t = int(input().rstrip())
for tc in range(t):
    k, n = map(int, input().rstrip().split())
    
    # m orig 을 k에 맞게 만든다.
    # m 도 똑같다
    m_orig.getKM(k)
    m.getKM(k)

    # (증요!!!!) m ^ n을 효과적으로 구한다
    # 없으면 시간초과
    # 문제 태그에 '분할 정복을 이용한 거듭제곱'.....
    m = power(m_orig, n)
    print(*m.m, sep='\n')

    # [1 0 0 ...] 와 곱한다.
    egg = [0] * (k + 1)
    egg[0] = 1
    egg = [egg]
    egg = Matrix(egg)
    egg *= m

    print(int(egg.m[0][0] % (1e8 + 7)))
    # 해당 답의 첫번째 원소가 답