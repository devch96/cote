def solution(arr1, arr2):
    return [[arr1[x][y] + arr2[x][y] for y in range(len(arr1[0]))] for x in range(len(arr1))]

"""
return [list(map(sum, zip(*x))) for x in zip(arr1, arr2)]
"""
