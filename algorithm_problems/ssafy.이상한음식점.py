def solution(foods):
    ascendingDP = foods[:]
    for start in range(len(foods)):
        for i in range(start + 1, len(foods)):
            if foods[i] > foods[start]:
                ascendingDP[i] += foods[i]
        print(foods[start], "가 지나감\n", ascendingDP)


if __name__ == '__main__':
    foods = [1, 9, 8, 3, 6, 3, 9, 5, 1, 4, 2]
    print(foods)
    print(solution(foods))