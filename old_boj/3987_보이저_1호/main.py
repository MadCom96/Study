def simul(tpr :int, tpc :int, td :int, n :int, m :int) -> bool:


n, m = map(int, input().split())

data = []

for i in range(n):
  data.append(input())

pr, pc = map(int, input().split())
d = 0
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]#  0 u    1 r    2 d    3 l

for i in range(4):
  tpr = pr
  tpc = pc
  td = d