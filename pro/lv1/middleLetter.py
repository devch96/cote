def solution(s):
    if len(s) % 2 == 0:
        return s[len(s)//2 -1] + s[len(s)//2]
    else:
        return s[len(s)//2]

"""
return s[(len(s)-1)//2 : len(str)//2+1]
"""
