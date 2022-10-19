def solution(arr, divisor):
    answer = [i for i in arr if i%divisor == 0]
    if len(answer) == 0:
        return [-1]
    return sorted(answer)

"""
return sorted([i for i in arr if i % divisor == 0] or [-1])
"""
