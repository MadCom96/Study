# 기사단원의 무기

def solution(number, limit, power):
    answer = 0

    for num in range(1, number + 1):
        last = 1
        count_devisor = 0
        for i in range(1, int(num ** (1/2)) + 1):
            if num % i == 0:
                last = i
                count_devisor += 2
        if last ** 2 == num:
            count_devisor -= 1
        if count_devisor > limit:
            answer += power
        else:
            answer += count_devisor
    
    return answer
    

if __name__ == "__main__":
    print(solution(5, 3, 2)) # 10
    print(solution(10, 3, 2)) # 21
    print(solution(9, 1, 1))