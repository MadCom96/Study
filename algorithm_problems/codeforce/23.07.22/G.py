t = int(input())

points = []

def isSameLine(i, j):
    global points
    if points[i][0] == points[j][0] or points[i][1] == points[j][1]:
        return True
    return False

def isDiag(i, j):
    global points
    if abs(points[i][1] - points[j][1]) == abs(points[i][0] - points[j][0]):
        return True
    return False

for _ in range(t):
    n = int(input())
    points = [(0, 0) for _ in range(n)]
    for i in range(n):
        x, y = map(int , input().split())
        points[i] = (x, y)
    
    ans = 0
    for i in range(n - 1):
        for j in range(i + 1, n):
            if isSameLine(i, j) or isDiag(i, j):
                ans += 1
    print(ans * 2)

