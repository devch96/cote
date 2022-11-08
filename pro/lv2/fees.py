def solution(fees, records):
    answer = []
    def minute(t):
        return int(t.split(":")[0])*60 + int(t.split(":")[1])
    dic = dict()
    for i in range(len(records)):
        records[i] = records[i].split(" ")
        dic[records[i][1]] = 0
    for time, car, inout in records:
        if inout == "IN":
            dic[car] -= minute(time)
        else: dic[car] += minute(time)
    for car, time in dic.items():
        if time <= 0:
            time = dic[car] + minute("23:59")
            print(dic)
        if time < fees[0]:
            dic[car] = fees[1]
        else:
            if ((time-fees[0])/fees[2])%1 == 0:
                dic[car] = fees[1] + ((time-fees[0])//fees[2]) * fees[3]
            else:
                dic[car] = fees[1] + (((time-fees[0])//fees[2])+1) * fees[3]

    dic = sorted(dic.items())
    print(dic)
    for i in dic:
        answer.append(int(i[1]))
    return answer
print(solution([180, 5000, 10, 600]	,["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]	 ))
print(solution([120, 0, 60, 591]	,["16:00 3961 IN","16:00 0202 IN","18:00 3961 OUT","18:00 0202 OUT","23:58 3961 IN"]	))
print(solution([1, 461, 1, 10],["00:00 1234 IN"]		))