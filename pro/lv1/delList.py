def solution(arr):
    if len(arr) <= 1:
        return [-1]
    del arr[arr.index(min(arr))]
    return arr

"""
if len(arr) <= 1:
    return [-1]
return [i for i in arr if i > min(arr)]
"""
