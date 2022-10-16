def solution(chicken):
    answer = 0
    while divmod(chicken,10)[0] >= 1:
        answer += divmod(chicken,10)[0]
        chicken = chicken // 10 + divmod(chicken,10)[1]
    return answer

"""
answer = (max(chicken,1)-1)//9
"""


