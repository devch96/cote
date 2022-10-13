def solution(n):
    def noComposite(num):
        if num == 1 or num == 2 or num == 3 : 
            return True                                 
        if num % 2 == 0 :
            return False
        for i in range(3,int(num**0.5)+1,2):                                           
            if num % i == 0:
                return False
        return True
    noC = 0
    for x in range(1,n+1):
        if noComposite(x):
            noC +=1
    return n - noC

"""
def is_compostie_num(num):
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return True
    return False
"""
