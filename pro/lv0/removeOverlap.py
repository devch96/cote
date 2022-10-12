def solution(my_string):
    answer = ''.join(list(dict.fromkeys(my_string).keys()))
    return answer

"""
from collections import OrderedDict
answer = ''.join(list(dict.fromkeys(my_string)))
"""

