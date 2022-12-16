#기사단원의 무기
def solution(number,limit,power):
    def countMeasure(n):
        temp = []
        for i in range(1,int(n**0.5)+1):
            if n % i == 0:
                if n != i **2:
                    temp.append(i)
                temp.append(n//i)
        return len(temp)
    temp = []
    for i in range(1,number+1):
        if countMeasure(i) > limit:
            temp.append(power)
        else:
            temp.append(countMeasure(i))
    return sum(temp)
print(solution(10,3,2))