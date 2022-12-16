#옹알이 (2)
def solution(babbling):
    check = {"aya":'!',"ye":'@',"woo":'#',"ma":'$'}
    answer = 0
    temp = []
    for s in babbling:
        for k,v in check.items():
            s = s.replace(k,v)
        temp.append(s)
        for i in range(len(s)-1):
            if s[i] == s[i+1]:
                if s in temp:
                    temp.remove(s)
    for i in temp:
        for s in '!@#$':
            i = i.replace(s,'')
        if i == '':
            answer += 1
    return answer

# def solution(babbling):
#     answer = 0
#     for i in babbling:
#         for j in ['aya','ye','woo','ma']:
#             if j*2 not in i:
#                 i = i.replace(j,' ')
#         if len(i.strip()) == 0:
#             answer += 1
#     return answer
print(solution(["ayaye","uuu","yeye","yemawoo","ayaayaa"]))
