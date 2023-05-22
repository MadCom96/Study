n, m = map(int, input().split())

nums = set(map(int, input().split()))
nums = list(nums)
nums.sort()
n = len(nums)

stack = []
done = set()

def dfs(ith, last_idx):
    global n, m, nums, stack, done

    for i in range(last_idx, n):
        stack.append(i)
        if ith == m:
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

dfs(1, 0)