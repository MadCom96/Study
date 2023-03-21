# 후보 추천하기
n = int(input())
rec_amount = int(input())
recommends = list(map(int, input().split()))

rec_count = [0 for _ in range(101)]
frame = []

for recommend in recommends:
    ifIn = False
    for f in frame:
        if f == recommend:
            ifIn = True
            break
    if ifIn:
        rec_count[recommend] += 1
    else:
        if len(frame) < n:
            frame.append(recommend)
            rec_count[recommend] += 1
        else:
            fewest = 1001
            fewest_idxs = []
            for fi in range(len(frame)):
                if rec_count[frame[fi]] < fewest:
                    fewest = rec_count[frame[fi]]
                    fewest_idxs = [fi]
                elif rec_count[f] == fewest:
                    fewest_idxs.append(fi)
            removed = frame.pop(fewest_idxs.pop(0))
            rec_count[removed] = 0
            rec_count[recommend] = 1
            frame.append(recommend)
print(*sorted(frame))