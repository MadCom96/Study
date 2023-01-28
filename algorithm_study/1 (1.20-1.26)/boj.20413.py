# MVP 다이아몬드 (Easy)

n = int(input())

silver, gold, platinum, diamond = map(int, input().split())
grades_log = input()

# 상민이의 여자친구: 상민이가 게임에 **최대** 얼마나 과금한건지 알려줘.
possible_highest = {"B": silver - 1, "S": gold - 1, "G": platinum - 1, "P": diamond - 1, "D": diamond}

s = 0
last_year = 0
for g in grades_log:
    if g == "D": # 한번 달성한 등급은 줄어들지 않는다.
        # 한달 최대 = 다이아몬드 등급 기준액
        s += diamond
        continue
    this_year = possible_highest[g] - last_year
    s += this_year
    last_year = this_year
print(s)
