def solution(answers):
    no1 = [1,2,3,4,5]
    count1 = 0
    no2 = [2,1,2,3,2,4,2,5]
    count2 = 0
    no3 = [3,3,1,1,2,2,4,4,5,5]
    count3 = 0
    for i in range(len(answers)):
        if answers[i] == no1[i%5]:
            count1 += 1
        if answers[i] == no2[i%8]:
            count2 += 1
        if answers[i] == no3[i%10]:
            count3 += 1
    result = [count1, count2, count3]
    return sorted([i+1 for i, n in enumerate(result) if n == max(result)])
