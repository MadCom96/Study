import sys
input = sys.stdin.readline

t = int(input())

sqrs = [i ** 2 for i in range(10001)]

s = []

def check(w, num): # 작거나 같으면 true
    total = 0
    for i in range(len(s)):
        total += (s[i] + 2 * w) ** 2
        if total > num:
            return False
    return True
    

for _ in range(t):
    n, c = map(int, input().split())
    s = list(map(int, input().split()))

    offset = 1000000
    for ss in s:
        if ss < offset:
            offset = ss
    
    diff = [-1] * n
    for i in range(n):
        diff[i] = s[i] - offset
    
    l = 0
    r = 10
    while True:
        if check(r, c):
            r *= 10
        else:
            break
    
    while l + 1 != r:
        m = (l + r) // 2
        if check(m, c):
            l = m
        else:
            r = m
    print(l)