def solution(dot):
    if dot[0] > 0 and dot[1] > 0:
        answer = 1
    elif dot[0] > 0 and dot[1] < 0:
        answer = 4
    elif dot[0] < 0 and dot[1] < 0:
        answer = 3
    else:
        answer = 2
    return answer

"""
a, b = 1 , 0
if dot[0]*dot[1] > 0:
    b = 1
if dot[1] <0:
    a = 2
return 2*a-b
"""
