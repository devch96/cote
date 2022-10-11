def solution(array, height):
    answer = 0
    for i in range(0, len(array)):
        if height < array[i]:
            answer += 1
    return answer

"""
array.append(height)
array.sort(reverse=True)
return array.index(height)
"""
