from collections import Counter
def solution(want, number, discount):
    answer = 0
    dic = {k:v for k,v in zip(want, number)}
    for i in range(len(discount) - sum(number)+1):
        tmp = discount[i:i+sum(number)]
        temp = Counter(tmp)
        if dic == Counter(tmp):
            answer += 1
    return answer
print(solution(["banana", "apple", "rice", "pork", "pot"],[3, 2, 2, 2, 1],["chicken", "apple", "apple", "banana", "rice", "apple", "pork", "banana", "pork", "rice", "pot", "banana", "apple", "banana"]))