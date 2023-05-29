n, m = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
stack = []
done = set()

def dfs(ith, last_idx):
    global n, m, nums, stack, done

    for i in range(last_idx + 1, n - (m - ith)):
        stack.append(i)
        # 마지막원소까지 채웠다면 
        if ith == m:
            # print(stack)
            tmp = []
            for i in range(len(stack)):
                tmp.append(nums[stack[i]])
            tmp = tuple(tmp)
            if tmp in done:
                pass
            else:
                done.add(tmp)
                print(*tmp)
        else:
            dfs(ith+1, i)
        stack.pop()

dfs(1, -1)