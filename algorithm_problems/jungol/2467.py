# 역순으로 해서 연결하면서 유니온파인드 하면 되지 않을까?
n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]
edges.sort(reversed= True)
# 일단 노드 번호는 1 ~ n이라고 가정하고 풀자. 조건이 없는듯

lim = 10*9

roots = [i for i in range(n + 1)]

def find(node) -> int:
    global roots
    return roots[node]

def union():
    pass



for edge in edges:
    # 한 줄씩 추가하면서 유니온 파인드

# in progress
