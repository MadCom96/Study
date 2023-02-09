# 양팔저울
num_weights = int(input())
weights = list(map(int, input().split()))

num_beads = int(input())
beads = list(map(int, input().split()))

dp = [False] * 40001
dp[0] = True
next_dp = []

for weight in weights:
    next_dp = dp[:]
    for i in range(0, 40001):
        if dp[i]:
            next_dp[abs(weight - i)] = True
            if weight + i < 40001:
                next_dp[weight + i] = True
    dp = next_dp

for bead in beads:
    if dp[bead]:
        print("Y")
    else:
        print("N")