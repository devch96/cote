def solution(emergency):
    answer = []
    for i in emergency:
        for j in sorted(emergency):
            if i == j:
                answer.append(len(emergency)-sorted(emergency).index(j))
    return answer

"""
return [sorted(emergency, reverse=True).index(e) + 1 for e in emergency]
"""
