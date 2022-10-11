def solution(slice, n):
    if n % slice == 0:
        answer = n / slice
    else:
        answer = (n // slice)+1
    return answer

"""
d , m = divmod(n, slize)
return d + int(m != 0)
"""
