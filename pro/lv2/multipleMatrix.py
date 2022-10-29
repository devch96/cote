def solution(arr1, arr2):
    return [[sum(a*b for a, b in zip(arr1_row, arr2_col)) for arr2_Col in zip(*arr2)] for arr1_row in arr1]

