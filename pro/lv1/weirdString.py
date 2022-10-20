def solution(s):
    answer = ''
    words = s.split(" ")
    for word in words:
        for idx , x in enumerate(word):
            if idx % 2 == 0:
                answer += x.upper()
            else:
                answer += x.lower()
        answer += ' '
    return answer[:-1]
print(solution("try hello world"))
