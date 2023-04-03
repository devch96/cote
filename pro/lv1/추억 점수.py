def solution(name, yearning, photo):
    answer = []
    scoredict = dict(zip(name,yearning))
    for i in photo:
        score = 0
        for j in i:
            if j in scoredict:
                score += scoredict.get(j)
        answer.append(score)
    return answer

print(solution(["may", "kein", "kain", "radi"],[5, 10, 1, 3],[["may", "kein", "kain", "radi"],["may", "kein", "brin", "deny"], ["kon", "kain", "may", "coni"]]))