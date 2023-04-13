import random as r

num = int(input())
for a in range(2, num + 1):
    b = r.randint(1, a - 1)
    print(f'{b} {a}')

for i in range(num):
    print(r.randint(0, 1), end=' ')