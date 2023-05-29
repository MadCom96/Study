def solution(sequence, k):
    n = len(sequence)

    max_sum = 0
    end = 0

    res = [0, n, n]
    for i in range(n):
        while max_sum < k and end < n:
            max_sum += sequence[end]
            end += 1
        if max_sum == k:
            newdata = [i, end-1, end-1-i]
            if newdata[2] < res[2]:
                res = newdata
        max_sum -= sequence[i]

    return res[:2]

# 누적합을 통해서 투포인터를 해도 그냥 투포인터보다 시간이 많이 걸리는데 왜그런건지..?
if __name__ == '__main__':
    sequence = [1, 2, 3, 4, 5]
    k = 7
    print(solution(sequence, k))

    sequence = [1, 1, 1, 2, 3, 4, 5]
    k = 5
    print(solution(sequence, k))

    sequence = [2, 2, 2, 2, 2]
    k = 6
    print(solution(sequence, k))

    sequence = [2, 2, 2, 2, 2]
    k = 10
    print(solution(sequence, k))