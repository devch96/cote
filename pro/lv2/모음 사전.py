def solution(word):
    dic = ['A','E','I','O','U']
    answer = 0
    for a in dic:
        answer += 1
        if a == word:
            return answer
        for b in dic:
            answer += 1
            if a + b == word:
                return answer
            for c in dic:
                answer += 1
                if a + b + c == word:
                    return answer
                for d in dic:
                    answer += 1
                    if a + b + c + d == word:
                        return answer
                    for e in dic:
                        answer += 1
                        if a + b + c + d + e == word:
                            return answer

print(solution("AAAAE"))
print(solution("I"))
