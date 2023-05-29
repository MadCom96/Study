def solution(e, starts):
    checker = [1 for i in range(e + 1)]
    lim = e
    for i in range(2, e + 1):
        ii = i * i
        if ii <= e:
            checker[i * i] += 1
            for j in range(i + 1, e + 1):
                if i * j <= e: 
                    checker[i * j] += 2
                else:
                    break
        else:
            break
    dp = [0 for i in range(e + 1)]
    highdp = -1
    highind = -1
    for i in range(len(checker)-1, 0, -1):
        if highdp <= checker[i]:
            highdp = checker[i]
            highind = i
        dp[i] = highind
    ans = []
    for s in starts:
        ans.append(dp[s])
    return ans


if __name__ == "__main__":
    print(solution(8, [1, 3, 7]))

# 1 8
# 2 4
# 3 3-> 9로 8보다 큼
# i j 역전
# 끝