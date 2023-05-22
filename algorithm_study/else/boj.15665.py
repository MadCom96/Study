n, m = map(int, input().split())

nums = set(map(int, input().split()))
nums = list(nums)
nums.sort()
n = len(nums)

stack = []
done = set()

def dfs(ith):
    global n, m, nums, stack, done

    for i in range(n):
        stack.append(i)
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
            dfs(ith+1)
        stack.pop()

dfs(1)