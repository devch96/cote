def solution(my_string, n):
    answer=''
    for i in my_string:
        answer += i*n
    return answer

"""
return ''.join(i*n for i in my_string)
"""

