def solution(s):
    result = []
    for i in range(len(s)):
        for j in range(i-1,-1,-1):
            if s[i] == s[j]:
                result.append(i-j)
                break
        else:
            result.append(-1)
    return result
print(solution("banana"))
print(solution("foobar"))