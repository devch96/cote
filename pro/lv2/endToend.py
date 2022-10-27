def solution(n, words):
    stack = []
    answer = [0,0]
    for x, y in enumerate(words):
        if not stack:
            stack.append(y)
            continue
        elif y in stack:
            return [(x%n)+1, (x+1)//n]
        elif stack[-1][-1] != y[0]:
            return [(x%n)+1, (x+1)//n]
        else:
            stack.append(y)
    return answer


