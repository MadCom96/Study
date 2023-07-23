from collections import deque

T = int(input())
for test_case in range(1, T + 1):
    v, e, a, b= map(int, input().split())
    children = [[] for _ in range(v + 1)]
    parents = [1 for _ in range(v + 1)]
    
    nums = list(map(int, input().split()))
    for i in range(0, len(nums), 2):
        p, c = nums[i], nums[i+1]
        children[p].append(c)
        parents[c] = p
    
    # a의 조상들을 모두 찾는다
    parentsset = set()
    p = a
    while True:
        parentsset.add(p)
        if p == 1:
            break
        p = parents[p]
    
    # b의 조상을 찾으면서 가장 낮을때 stop
    ans = -1
    p = b
    while True:
        if p in parentsset:
            ans = p
            break
        p = parents[p]
    
    size = 1
    q = deque([ans])
    while q:
        node = q.popleft()
        size += len(children[node])
        for c in children[node]:
            q.append(c)
    print(f'#{test_case} {ans} {size}')