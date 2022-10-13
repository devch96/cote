def solution(array,n):
    answer = 0
    array.append(n)
    array.sort()
    s = array.index(n)
    if len(array) == s+1:
        answer = array[s-1]
    elif array[s-1] == array[s+1]:
        answer = array[s-1]
    elif abs(array[s-1] - n) > array[s+1] - n:
        answer = array[s+1]
    else:
        answer = array[s-1]
    return answer
