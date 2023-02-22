# 후보키
from itertools import combinations

def isUnique(comb: set, relation: list):
    comb = tuple(comb)
    all = set()
    for r in relation:
        a = []
        for c in comb:
            a.append(r[c])
        all.add(tuple(a))
    if len(all) == len(relation):
        return True
    return False


def solution(relation: list):
    answer = 0
    info_len = len(relation[0])
    sample = [i for i in range(info_len)]
    candidates = []
    for size in range(1, info_len + 1):
        # 사이즈에 맞는 쌍을 만들고
        for comb in combinations(sample, size):
            print(comb)
            csize = len(comb)
            isMinimal = True
            # 이전 가능했던 쌍과 겹치는지 검사하여 뺀다? -> 최소성 검사
            for can in candidates:
                temp = set(comb)
                for cc in can:
                    temp.add(cc)
                if csize == len(temp):
                    isMinimal = False
                    break
        # 유일성 검사
        # 검사를 통과한 만큼 answer += 1 
            if isMinimal:
                if isUnique(comb, relation):
                    answer += 1
                    candidates.append(comb)
    return answer


# 검사순서
# 1o 2x 3x 4x
# 12- 13- 14- 23o 24x 34x
# 123- 124- 234-
# 1234-

if __name__ == '__main__':
    print(solution([
        ["100","ryan","music","2"],
        ["200","apeach","math","2"],
        ["300","tube","computer","3"],
        ["400","con","computer","4"],
        ["500","muzi","music","3"],
        ["600","apeach","music","2"]
    ]))