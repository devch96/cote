def solution(dartResult):
     dartResult = list(dartResult)
     r = []

     for i in range(len(dartResult)):
         if dartResult[i] == 'S':
             r[-1] **= 1
         elif dartResult[i] == 'D':
             r[-1] **= 2
         elif dartResult[i] == 'T':
             r[-1] **= 3
         elif dartResult[i] == '*':
             r[-1] *= 2
             if len(r)>1:
                 r[-2] *= 2
         elif dartResult[i] == '#':
             r[-1] *= -1
         elif dartResult[i] == '1' and dartResult[i+1] == '0':
             r.append(10)
             dartResult[i+1] = '-'
         elif dartResult[i] != '-':
             r.append(int(dartResult[i]))

     answer = sum(r)
     return answer
