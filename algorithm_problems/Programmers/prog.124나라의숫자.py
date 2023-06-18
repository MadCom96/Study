sizes = []
def solution(n):
    global sizes

    sizes = [0, 3]
    
    while sizes[-1] < n:
        sizes.append(sizes[-1] + 3 ** len(sizes))
        
    th = n - sizes[-2] - 1
    
    times = len(sizes) - 1
    ans = ''
    for _ in range(times):
        ans = '124'[th%3] + ans
        th //= 3
    return ans

for i in range(1, 100):
    print(solution(i))
