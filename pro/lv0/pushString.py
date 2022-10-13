def solution(A, B):
    answer = -1
    if A == B:
        return = 0
    temp = list(A)
    for i in range(1,len(A)+1):
        temp.insert(0,temp.pop())
        a = ''.join(temp)
        if a == B:
            answer = i
    return answer
        
o
 o
  o
   o
    o
     
hello
