import random as r

print(20, 10)
for i in range(20):
    for j in range(10):
        if j == 0 or j == 19:
            print('.', end='')
        else:
            posi = r.uniform(1, 10)
            if posi < 2.6:
                print('x', end='')
            else:
                print('.', end='')
    print()