def min(a, b):
  if a < b:
    return a
  return b

def max(a, b):
  if a > b:
    return a
  return b

impsb = [[], [0,0,0,2,0,0,0,4,0,5], [0,0,0,0,0,0,0,0,5,0], [0,0,0,0,0,0,0,5,0,0],\
[0,0,0,0,0,0,5,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,8],\
[0,0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0,0]]

while True:
  v = [False for i in range(10)]
  l = int(input())
  nums = list(map(int,input().split()))

  nosig = False
  for i in range(1, l):
    hi = max(nums[i - 1], nums[i])
    lo = min(nums[i - 1], nums[i])
    v[nums[i - 1]] = True
    if v[nums[i]]:
      print('NO')
      nosig = True
      break
    if impsb[lo][hi] != 0:
      if v[impsb[lo][hi]]:
        continue
      else:
        print('NO')
        nosig = True
        break

  if nosig != True:
    print('YES')