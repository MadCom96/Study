def solution(s):
    ans = 0
    pair = {'{':'}', '[':']', '(':')'}
    for _ in range(len(s)):
        iscorrect = True
        stack = []
        for v in s:
            if v in ['{','[','(']:
                stack.append(v)
            elif not stack or v != pair[stack[-1]]:
                iscorrect = False
            else:
                stack = stack[:-1]

        print(iscorrect, stack)
        ans += int(iscorrect and not stack)
        s = s[1:]+s[0]

    return ans