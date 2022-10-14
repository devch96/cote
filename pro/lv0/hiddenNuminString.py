def solution(my_string):
    temp = ''.join((i if i in '0123456789' else ' ')for i in my_string)
    answer = [int(i) for i in temp]
    return sum(answer)

"""
import re
return sum(map(int, re.findall(r"\d+", my_string)))
"""
