def solution(players, callings):
    dic = {k:v for v,k in enumerate(players)}
    dic1 = {v:k for k,v in dic.items()}

    for call in callings:
        now = dic.get(call) #이름 불린애 등수
        before = dic1.get(now-1) #앞서있는 애 이름
        dic[call] -=1 # 등수 -1
        dic[before] += 1 #앞서있는애 등수 +1
        dic1[now] = dic1.pop(now-1)
        dic1[now-1] = call
    
    answer = [player for player, rank in sorted(dic.items(), key=lambda x : x[1])]
    return answer
print(solution(["mumu", "soe", "poe", "kai", "mine"],["kai", "kai", "mine", "mine"]))