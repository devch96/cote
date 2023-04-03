def solution(t,p):
    answer = 0
    for i in range(0,len(t)-len(p)+1):
        temp = int(t[i:i+len(p)])
        if temp <= int(p):
            answer += 1
    return answer
print(solution("3141592","271"))
print(solution("500220839878","7"))
print(solution("10203","15"))