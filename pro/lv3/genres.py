#베스트앨범
def solution(genres, plays):
    answer = []
    dic = dict()
    dic2 = dict()
    for i in range(len(genres)):
        if genres[i] in dic:
            dic[genres[i]].append((plays[i],i))
            dic2[genres[i]] += plays[i]
        else:
            dic[genres[i]] = [(plays[i],i)]
            dic2[genres[i]] = plays[i]
    rank = sorted(dic2, key = lambda x : dic2[x], reverse = True)
    for i in rank:
        temp = sorted(dic[i], key = lambda x:(x[0],-x[1]), reverse = True)
        for j in range(2):
            if temp:
                answer.append(temp.pop(0)[1])
    return answer
print(solution(["classic", "pop", "classic", "classic", "pop"], [500,600,150,800,2500]))