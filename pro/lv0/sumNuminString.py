def solution(my_string):
    answer = 0
    for i in my_string:
        if i.isdigit():
            answer += int(i)
    return answer

"""
return sum(int(i) for i in my_string if i.isdigit())

import re
return sum(int(n) for n in re.sub('[^1-9]','',my_string))
"""
