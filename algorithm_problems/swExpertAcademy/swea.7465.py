# 창용 마을 무리의 개수
root = []

def find(a):
    global root
    if root[a] == a:
        return a
    else:
        ans = find(root[a])
        root[a] = ans
        return ans


def union(a, b):
    global root
    aa = find(a)
    bb = find(b)
    root[bb] = aa

test_case = int(input())
for tc in range(test_case):
    n, m = map(int, input().split())
    root = [i for i in range(n+1)]
    for _ in range(m):
        a, b = map(int, input().split())
        union(a, b)
    counter = set()
    for i in range(1, n+1):
        counter.add(find(i))
    print(f'#{tc + 1} {len(counter)}')