def solution(answers):
    a1 = [1,2,3,4,5]
    a2 = [2,1,2,3,2,4,2,5]
    a3 = [3,3,1,1,2,2,4,4,5,5]
    s1 = 0
    s2 = 0
    s3 = 0
    for i in range(len(answers)):
        if answers[i] == a1[i%5]:
            s1 += 1
        if answers[i] == a2[i%8]:
            s2 += 1
        if answers[i] == a3[i%10]:
            s3 += 1
    answer = [s1,s2,s3]
    return sorted(i+1 for i, n in enumerate(answer) if n == max(answer))
print(solution([1,3,2,4,2]))