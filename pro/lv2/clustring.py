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


# def solution(str1, str2):
#     s1 = make_2_word(str1)
#     s2 = make_2_word(str2)
#     if s1 == [] and s2 == []:
#         return 65536

#     s1_copy = s1.copy()
#     s2_copy = s2.copy()

#     # 교집합
#     inter = []
#     for i in s1:
#         if i in s2_copy:
#             inter.append(i)
#             s1_copy.remove(i)
#             s2_copy.remove(i)


#     # 합집합
#     union = inter + s1_copy + s2_copy


#     answer = int((len(inter) / len(union)) * 65536)
#     print(inter,union)
#     return answer


# def make_2_word(s):
#     s = s.upper()
#     a = []
#     for i in range(len(s) - 1):
#         if s[i:i + 2].isalpha():
#             a.append(s[i:i + 2])
#     return a
print(solution("FRANCE","french"))
print(solution("handshake","shake hands"))