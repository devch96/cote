def solution(s):
    answer = 0
    for i in range(len(s)):
        if i != 0 :
            s = s[1:] + s[0]
        stack = []
        for q in s:
            if stack:
                if stack[-1] == '[' and q == ']': 
                    stack.pop()
                elif stack[-1] == '{' and q == '}':
                    stack.pop()
                elif stack[-1] == '(' and q == ')':
                    stack.pop()
                else:
                    stack.append(q)
            else:
                stack.append(q)

        if len(stack) == 0:
            answer += 1
    return answer
