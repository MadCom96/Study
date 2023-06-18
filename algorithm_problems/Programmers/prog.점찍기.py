def pita_sub(d, a):
    return (d ** 2 - a ** 2) ** 0.5

def solution(k, d):
    cnt = 0
    for a in range(0, d+1, k):
        b = pita_sub(d, a)
        cnt += int(b) // k + 1
    return cnt

if __name__ == "__main__":
    k = 2
    d = 4
    print(solution(k, d))

    k = 1
    d = 5
    print(solution(k, d))