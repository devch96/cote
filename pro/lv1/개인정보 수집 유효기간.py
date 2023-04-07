def solution(today, terms, privacies):
    answer = []
    today = int(today.replace(".",""))
    dic = dict()
    for i in terms:
        dic[i.split()[0]] = int(i.split()[1])
    for i in range(len(privacies)):
        privacy = privacies[i].split()[0]
        term = dic.get(privacies[i].split()[1])
        p_year, p_month, p_day = map(int,privacy.split("."))
        if term < 12:
            if p_month + term > 12:
                p_month = p_month+term - 12
                p_year +=1
            else:
                p_month += term
        else:
            p_year += (p_month+term)//12
            p_month = (p_month+term) - (((p_month+term)//12)*12)

        if p_day == 1:
            p_day = 28
            if p_month == 1:
                p_month = 12
                p_year -= 1
            else:
                p_month -= 1
        else:
            p_day -= 1

        if p_month < 10:
            p_month = "0"+str(p_month)

        if p_day < 10:
            p_day = "0"+str(p_day)
        pp = int(str(p_year) + str(p_month) + str(p_day))
        if today > pp:
            answer.append(i+1)
    return answer
# print(solution("2022.05.19",["A 6", "B 12", "C 3"],["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]))
# print(solution("2020.01.01",["Z 3", "D 5"],["2019.01.01 D", "2019.11.15 Z", "2019.08.02 D", "2019.07.01 D", "2018.12.28 Z"]))
# print(solution("2024.06.08",["A 18"],["2022.06.08 A"]))
# print(solution("2019.01.01",["B 12"],["2017.12.21 B"]))
# print(solution("2019.01.01",["A 12"],["2017.12.21 A"]))
print(solution("2022.02.28",["A 23"], ["2020.01.28 A"]))