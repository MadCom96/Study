import sys
fo = open("input.txt")
sys.stdin = fo

test_case = int(input())
for tc in range(test_case):
    t = int(input())
    students = list(map(int, input().split()))
    counter = [0] * 101
    for student in students:
        counter[student] += 1
    
    highest = 0
    highestidx = 0
    for i in range(101):
        if counter[i] >= highest:
            highest = counter[i]
            highestidx = i

    print(f'#{t} {highestidx}')