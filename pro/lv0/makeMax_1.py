def solution(numbers):
    numbers.sort()
    answer = numbers.pop() * numbers.pop()
    return answer

"""
return sorted(numbers)[-1] * sorted(numbers)[-2]
"""

