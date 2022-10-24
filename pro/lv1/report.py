def solution(id_list, report, k):
    id_report = dict()
    id_result = dict()
    temp = []
    for i in id_list:
        id_report[i] = 0
        id_result[i] = 0

    for x in set(report):
        temp.append(x.split(' '))
        user1, user2 = x.split(' ')
        id_report[user2] += 1

    result = [x for x, y in id_report.items() if y >= k]
    for a in temp:
        if a[1] in result:
            id_result[a[0]] +=1
    return list(id_result.values())

print(solution(["muzi", "frodo", "apeach", "neo"],["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"],2))
print(solution(["con", "ryan"],["ryan con", "ryan con", "ryan con", "ryan con"],3))

"""
answer = [0] * len(id_list)
reports = {x:0 for x in id_list}

for i in set(report):
    reports[i.split()[1]] += 1

for i in set(report):
    if reports[i.split()[1]] >= k:
        answer[id_list.index(i.split()[0])] +=1

return answer
"""
