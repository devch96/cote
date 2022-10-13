def solution(common):                                                                  
    answer = 0                                                                         
    if common[2]-common[1] == common[1]-common[0]:
        answer = max(common)+(common[1]-common[0])
    elif common[2]/common[1] == common[1]/common[0]:
        answer = max(coomon)*(common[1]/common[0])
    return answer








"""
    def d(n):                                                                          
        return common[n+1] - common[n]                                                 
    def r(n):                                                                          
        return common[n+1] // common[n]                                                
    for i in range(len(common)-1):                                                     
        if d(i) == d(i+1):                                                             
            answer = common[-1] + d(1)                                                
        elif r(i) == r(i+1):                                                           
            answer = common[-1] * r(1)                                                
    return answer
"""
