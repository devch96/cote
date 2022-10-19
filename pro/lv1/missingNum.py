def solution(numbers):
    num = set([1,2,3,4,5,6,7,8,9,0])
    return sum(list(num - set(numbers)))

"""
return sum([i for i in range(10) if i not in numbers])
"""
