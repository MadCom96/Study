# boj 2042번 문제 구간 합 구하기
import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())
nums = [int(input()) for _ in range(n)]

tree = [0] * (4*n)

def init(start, end, node):
    global tree
    if start == end:
        tree[node] = nums[start]
        return tree[node]
    mid = (start + end) // 2
    tree[node] = init(start, mid, node * 2) + init(mid+1, end, node*2+1)
    return tree[node]

def getSum(start, end, node, left, right):
    global tree
    if left > end or right < start:
        return 0
    if left <= start and end <= right:
        return tree[node]
    mid = (start + end) // 2
    return getSum(start, mid, node * 2, left, right)\
        + getSum(mid + 1, end, node *2 +1, left, right)

def update(start, end, node, index, dif):
    global tree
    if index < start or index > end:
        return
    tree[node] += dif
    if start == end:
        return
    mid = (start + end) // 2
    update(start, mid, node * 2, index, dif)
    update(mid + 1, end, node * 2 + 1, index, dif)

# def showtree():
#     global tree
#     start = 1
#     for i in range(len(tree)):
#         if i == start:
#             start *= 2
#             print()
#         print(f'{tree[i]}\t', end='')

init(0, n-1, 1)
# showtree()
for _ in range(m+k):
    a, b, c = map(int, input().split())
    if a == 1:
        update(0, n-1, 1, b-1, c-nums[b-1])
        nums[b-1] = c
        # showtree()
    else:
        print(getSum(0, n-1, 1, b-1, c-1))

        