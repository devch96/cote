def solution(str1, str2):
    str1 = str1.lower()
    str2 = str2.lower()
    X = [str1[i:i+2] for i in range(len(str1)-1) if str1[i:i+2].isalpha()]
    Y = [str2[i:i+2] for i in range(len(str2)-1) if str2[i:i+2].isalpha()]
    if X == [] and Y == []:
         return 65536
    inter = []
    x1 = X.copy()
    y1 = Y.copy()
    for i in x1[:]:
        if i in y1:
            inter.append(i)
            x1.remove(i)
            y1.remove(i)
    union = inter + x1 + y1
    print (inter, union)
    answer = int((len(inter)/len(union))*65536)
    return answer
print(solution("FRANCE","french"))
print(solution("handshake","shake hands"))