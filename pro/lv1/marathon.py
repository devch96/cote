def solution(participant, completion):
    if set(participant) != set(completion):
        return list(set(participant) - set(completion))[0]
    else:
        dic = dict()
        for i in participant:
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1

        for i in completion:
            if dic[i] == 1:
                del dic[i]
            else:
                dic[i] -= 1
        return list(dic.keys())[0]
