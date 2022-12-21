from collections import Counter
def solution(k, tangerine):
    tC = sorted(Counter(tangerine).values(),reverse=True)
    temp = 0
    answer = 0
    for i in tC:
        temp += i
        answer += 1
        if temp >= k:
            break
    return answer
print(solution(6,[1,3,2,5,4,5,2,3]))
print(solution(4,[1,3,2,5,4,5,2,3]))
print(solution(2,[1,1,1,1,2,2,3]))