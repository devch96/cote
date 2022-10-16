def solution(score):
    score = [sum(i) for i in score]
    dic = dict()
    for i, j in enumerate(sorted(score, reverse=True)):
        if j not in dic:
            dic[j] = i+1

    answer = [dic[i] for i in score]
    return answer
