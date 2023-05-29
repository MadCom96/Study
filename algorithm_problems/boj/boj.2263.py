# 트리의 순회
import sys
sys.setrecursionlimit(10**5)

n = int(input())
inO = list(map(int, input().split()))
postO = list(map(int, input().split()))

# l 현재 분할된 부분의 가장 왼쪽 인덱스
# r 현재 분할된 부분의 가장 오른쪽 인덱스
def findInInO(l, r, node):
    global inO
    for i in range(l, r+1):
        if inO[i] == node:
            return i

def sol(inl, inr, postl, postr):
    global inO, postO
    if inl == inr:
        print(inO[inl], end=' ')
        return
    if inl > inr or postl > postr:
        return
    topNode = postO[postr]
    print(topNode, end=' ')
    splitPoint1 = findInInO(inl, inr, topNode)
    # inl ~ splitpoint1까지 하면 왼쪽 트리의 갯수가 나온다
    splitPoint2 = postl - 1 + splitPoint1 - inl
    sol(inl, splitPoint1-1, postl, splitPoint2)
    sol(splitPoint1+1, inr, splitPoint2+1, postr-1)

sol(0, n-1, 0, n-1)