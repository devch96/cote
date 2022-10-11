def solution(my_string):
    my_string = sorted(my_string.lower())
    answer = ''.join(i for i in my_string)
    return answer

"""
answer = "".join(sorted(list(my_string.lower())))
return answer
"""
