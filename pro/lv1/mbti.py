def solution(survey, choices):
    mbti1 = {"R":0,"T":0}
    mbti2 = {"C":0,"F":0}
    mbti3 = {"J":0,"M":0}
    mbti4 = {"A":0,"N":0}
    score  = [3,2,1,0,-1,-2,-3]
    for i in range(len(survey)):
        if survey[i] == "RT" or survey[i] == "TR":
            mbti1[survey[i][0]] += score[choices[i]-1]
        elif survey[i] == "CF" or survey[i] == "FC":
            mbti2[survey[i][0]] += score[choices[i]-1]
        elif survey[i] == "JM" or survey[i] == "MJ":
            mbti3[survey[i][0]] += score[choices[i]-1]
        else:
            mbti4[survey[i][0]] += score[choices[i]-1]

    answer = ''
    if sum(mbti1.values()) == 0:
        answer += sorted(mbti1.keys())[0]
    else:
        answer += max(mbti1, key = mbti1.get)

    if sum(mbti2.values()) == 0:                               
        answer += sorted(mbti2.keys())[0]                      
    else:                                                      
        answer += max(mbti2, key = mbti2.get)
    
    if sum(mbti3.values()) == 0:
        answer += sorted(mbti3.keys())[0]
    else:
        answer += max(mbti3, key = mbti3.get)

    if sum(mbti4.values()) == 0:
        answer += sorted(mbti4.keys())[0]
    else:
        answer += max(mbti4, key = mbti4.get)

    return answer
print(solution(["TR","RT","TR"],[7,1,3]))
print(solution(["AN","CF","MJ","RT","NA"],[5,3,2,7,5]))
