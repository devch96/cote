def solution(i,j,k):
    temp = ""
    for i in range(i,j+1):
        temp += str(i)
    answer = temp.count(str(k))
    return answer

"""
return sum([str(i).count(str(k)) for i in range(i,j+1)])
"""
