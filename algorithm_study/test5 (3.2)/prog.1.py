# 성격 유형 검사하기


def solution(survey, choices):
    kbti = {'R':0, 'T':0, 'C':0, 'F':0, 'J':0, 'M':0, 'A':0, 'N':0}
    for i in range(len(survey)):
        if choices[i] == 1:
            kbti[survey[i][0]] += 3
        elif choices[i] == 2:
            kbti[survey[i][0]] += 2
        elif choices[i] == 3:
            kbti[survey[i][0]] += 1
        elif choices[i] == 4:
            pass
        elif choices[i] == 5:
            kbti[survey[i][1]] += 1
        elif choices[i] == 6:
            kbti[survey[i][1]] += 2
        elif choices[i] == 7:
            kbti[survey[i][1]] += 3

    ans = ''

    if kbti['R'] >= kbti['T']:
        ans = ans + 'R'
    else:
        ans = ans + 'T'
    if kbti['C'] >= kbti['F']:
        ans = ans + 'C'
    else:
        ans = ans + 'F'
    if kbti['J'] >= kbti['M']:
        ans = ans + 'J'
    else:
        ans = ans + 'M'
    if kbti['A'] >= kbti['N']:
        ans = ans + 'A'
    else:
        ans = ans + 'N'
    return ans