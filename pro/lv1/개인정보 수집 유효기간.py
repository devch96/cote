def solution(today, terms, privacies):
    today = today.replace(".","")
    dic = dict()
    answer = []
    for i in terms:
        dic[i.split()[0]] = int(i.split()[1])
    
    for i in range(len(privacies)):
        privacy = privacies[i].split()[0]
        term = dic.get(privacies[i].split()[1])
        p_year, p_month, p_day = map(int, privacy.split("."))

        t_year = term // 12
        t_month = term % 12

        p_day -= 1
        p_month += t_month
        p_year += t_year

        if(p_day == 0):
            p_day = 28
            p_month -= 1
            if(p_month == 0):
                p_month = 12
                p_year -= 1
        if(p_month%12 != 0):
            p_year += p_month//12
            p_month %= 12

        if p_month < 10:
            p_month = "0"+str(p_month)
        else:
            p_month = str(p_month)
        if p_day < 10:
            p_day = "0"+str(p_day)
        else:
            p_day = str(p_day)
        p_year = str(p_year)

        if int(today) > int(p_year+p_month+p_day):
            answer.append(i+1)

        
    return answer
print(solution("2024.12.19",["A 24"],["2022.12.19 A"]))
