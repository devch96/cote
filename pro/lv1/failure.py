def solution(N, stages):
    temp = []
    for i in range(1,N+1):
        if stages.count(i) > 0 :
            temp.append([i,stages.count(i)/len([x for x in stages if x >= i])])
        else:
            temp.append([i,0])
    temp.sort(key = lambda x : x[1], reverse = True)
    return [x for x, y in temp]
print(solution(5, [2,1,2,6,2,4,3,3]))
