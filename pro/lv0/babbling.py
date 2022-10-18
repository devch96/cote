def solution(babbling):
    can = ["aya","ye","woo","ma"]
    for i in can:
        for j in range(len(babbling):
            if i + i in babbling[j]:
                continue
            babbling[j] = babbling[j].replace(i,"")
    answer = babbling.count("")
    return answer
