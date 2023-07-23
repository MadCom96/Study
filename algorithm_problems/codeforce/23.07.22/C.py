t = int(input())
for _ in range(t):
    s = ''
    for y in range(8):
        line = input()
        for x in range(8):
            if line[x] == '.':
                continue
            s = s + line[x]
    print(s)