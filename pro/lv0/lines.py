def solution(lines):
    temp = []
    for a in lines:
        temp.append(sorted(a))
    x = set(i for i in range(temp[0][0],temp[0][1]))
    y = set(i for i in range(temp[1][0],temp[1][1]))
    z = set(i for i in range(temp[2][0],temp[2][1]))

    if len(x&y&z) == len(x|y|z):
        answer = len(x|y|z)
    elif len(x&y&z) >= 1 :
        answer = len(x&y) + len(y&z) + len(z&x) - len(x&y&z)*2
    else:
        answer = len(x&y) + len(y&z) + len(z&x)
    return answer

"""
sets = [set(range(min(l),max(l))) for l in lines]
return len(sets[0] & sets[1] | sets[1] & sets[2] | sets[2] & sets[0])
"""
