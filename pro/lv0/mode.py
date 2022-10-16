def solution(array):
    answer = 0
    dic = {}
    for i in array:
        if i not in dic:
            dic[i] = array.count(i)
    temp = [i for i in dic.values()]
    if temp.count(max(temp)) >= 2:
        return -1
    for a, b in dic.items():
        if b == max(temp):
            answer = a

    return answer
    
