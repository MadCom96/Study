def pushin(scedule, loc, v):
  while len(scedule) <= loc:
    scedule.append(-1)
  small = -1
  smallind = -1
  for i in range(loc, 0, -1):
    if scedule[i] == -1:
      scedule[i] = v
      return
    else:
      if smallind == -1:
        smallind = i
        small = scedule[i]
      else:
        if small > scedule[i]:
          smallind = i
          small = scedule[i]
  if small < v:
    scedule[smallind] = v
  
        
#main
n = int(input())
scedule = []

for _ in range(n):
  p, d = map(int, input().split())
  pushin(scedule, d, p)
  #print(scedule)#제출시 주석처리하자
total = 0
for v in scedule:
  if v != -1:
    total += v
print(total)