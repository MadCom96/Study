import random as r

tc = 1000000
testing = True

goat = "goat"
sports_car = "sports car"

cnt = 0
for test_case in range(tc):
    doors = [goat, goat, sports_car]
    # 문 뒤에 랜덤으로 염소2마리와 스포츠카를 배치한다
    r.shuffle(doors)
    if testing:
        print(f"#{test_case+1} 번째 실험")
        print(doors)

    # 무조건 0번을 고른다고 한다 (0, 1, 2 중)
    pick = 0
    # 고르지 않은 문 중 염소가 있는 문 하나를 열어준다
    for i in range(1, 3):
        if doors[i] == goat:
            doors.pop(i)
            break
    # 선택을 바꾼다
    pick = 1

    if testing:
        print(f'========= {doors[pick]} =========')
        print()

    if doors[pick] == sports_car:
        cnt += 1
    
print(f'{cnt} / {tc}')
print(f'{cnt / tc * 100} % 확률로 {sports_car} 획득!')