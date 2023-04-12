def solution(numbers):
    answer = []
    # for i in numbers:
    #     if i % 4 == 3:
    #         Temp = '0' + bin(i)[2:]
    #         for i in range(len(Temp)-1, -1, -1):
    #             if Temp[i] == '0':
    #                 answer.append(int(Temp[0:i] + "10" + Temp[i+2:],2))
    #                 break
    #     else:
    #         answer.append(i+1)
    for num in numbers:
        answer.append(((num ^ (num+1)) >> 2 ) +num + 1)
    return answer

print(solution([2,7]))
print(solution([1001,337,0,1,333,673,343,221,898,997,121,1015,665,779,891,421,222,256,512,128,100]))