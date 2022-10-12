def solution(num,k):
    answer = -1
    temp = list(str(num))
    for i in range(len(temp)):
        if temp[i] == str(k):
            answer = i
            break
    return answer

"""
answer = (str(num).find(str(k))+1)
if answer == 0:
    answer = -1
return answer
"""
