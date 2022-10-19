def solution(absolutes, signs):
    answer = 0
    for i in range(len(absolutes)):
        if signs[i]:
            answer += absolutes[i]
        else:
            answer -= absolutes[i]
    return answer

"""
return sum(absolutes if sign else -absolutes for absolutes, sign in zip(absolutes, signs))
"""
