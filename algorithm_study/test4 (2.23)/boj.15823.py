# 카드 팩 구매하기
n, m = map(int, input().split())
cards = list(map(int,input().split()))

find_from = 0
find_value = 0
card_set = set()
# 다음 검사할 idx를 find from으로 주고, 찾았는지 여부를 반환
def find_one() -> bool: 
    global n, m, cards, find_from, find_value, card_set
    card_set.clear()
    for i in range(find_from, find_from + find_value):
        first = len(card_set)
        card_set.add(cards[i])
        second = len(card_set)
        if first == second:
            same = cards[i]
            for i in range(find_from, find_from + find_value):
                if cards[i] == same:
                    find_from = i + 1
                    return False
    find_from = find_from + find_value
    return True


def check() -> bool:
    global n, m, cards, find_from, find_value
    cnt = 0
    while True:
        if n - ((m - cnt) * find_value) < find_from:
            break
        if find_one():
            cnt += 1
            if cnt == m:
                return True
    return False


l = 1
r = n // m + 1
while l + 1 != r:
    mid = (l + r) // 2
    find_value = mid
    find_from = 0
    if check():
        l = mid
    else:
        r = mid
print(l)
