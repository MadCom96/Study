import math as m

def solution(r1, r2):
    cnt = r2 - r1 + 1
    for y in range(1, r1):
        a = m.sqrt(r1**2 - y**2)
        b = m.sqrt(r2**2 - y**2)
        ia = int(a)
        ib = int(b)
        cnt += ib - ia
        if ia == a:
            cnt += 1

    for y in range(r1, r2):
        b = m.sqrt(r2**2 - y**2)
        ib = int(b)
        cnt += ib
    
    return 4 * cnt

if __name__ == '__main__':
    print(solution(2, 3))