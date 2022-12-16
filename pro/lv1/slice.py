def solution(s):
    answer = 0
    while s:
        i, o = 0,0
        for x in s:
            if x == s[0]:
                i += 1
            else:
                o += 1
            if i == o:
                break
        s = s[i+o:]
        answer += 1
    return answer
print(solution("banana"))
print(solution('aaabb'))