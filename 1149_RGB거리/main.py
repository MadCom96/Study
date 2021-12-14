def min(a, b):
  if a < b:
    return a
  else:
    return b

n = int(input())

R = []
G = []
B = []

r, g, b = map(int,input().split())
R.append(r)
G.append(g)
B.append(b)
for _ in range(n - 1):
  r, g, b = map(int,input().split())
  R.append(min(G[_] + r, B[_] + r))
  G.append(min(R[_] + g, B[_] + g))
  B.append(min(G[_] + b, R[_] + b))
  
print(min(min(G[n - 1], R[n - 1]), B[n - 1]))