def solution(record):
    id_list = {i.split()[1]:i.split()[2] for i in record if len(i.split()) == 3}
    def sendMsg(inout, userid):
        if inout == 'Enter':
            return '{userid}님이 들어왔습니다.'.format(userid = id_list[userid])
        else:
            return '{userid}님이 나갔습니다.'.format(userid = id_list[userid])   
    answer = []
    for i in record:
        if i.split()[0] == 'Change':
            continue
        answer.append(sendMsg(i.split()[0], i.split()[1]))
    return answer
print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))
    