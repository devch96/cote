def solution(s):
    answer = ''
    for i in set(a):
        if s.count(i) == 1:
            answer += i
    a = ''.join(sorted(answer))
    return a

"""
answer = "".join(sorted([ch for ch in s if s.count(ch) == 1]))
"""

