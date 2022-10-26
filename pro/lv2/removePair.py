def solution(s):
    stack = []
    for i in s:
        if not stack:
            stack.append(i)
        elif stack[-1] == i:
            stack.pop()
        else:
            stack.append(i)

    if not stack:
        return 1
    else:
        return 0

"""
return not(stack)
"""
