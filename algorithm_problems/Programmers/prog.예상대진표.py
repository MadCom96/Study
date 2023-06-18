def solution(n,a,b):
    a -= 1
    b -= 1
    astr = ''
    bstr = ''
    for i in range(21):
        if a % 2 == 1:
            astr = '1' + astr
        else:
            astr = '0' + astr

        if b % 2 == 1:
            bstr = '1' + bstr
        else:
            bstr = '0' + bstr
        
        a //= 2
        b //= 2
    
    here = -1
    for i in range(21):
        if bstr[i] != astr[i]:
            here = i
            break
    return 21 - i

# 이진수로 푸는 아이디어는 좋으나 
# xor과 bit_length 등을 이용하여 더 짧게 풀 수 있음