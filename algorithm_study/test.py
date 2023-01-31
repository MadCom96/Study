import random as r

for i in range(10):
    print(chr(r.randint(0, 2) + ord('a')), end='')
print()
for i in range(5):
    print(chr(r.randint(0, 5) + ord('a')), end='')
print()

01 23 456 7 89
ac ab bbc a ac
bafbc