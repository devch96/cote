def solution(s):
    answer = []
    s = s[:-2].replace('{','').replace(',',' ').split('}')
    
    for i,v in enumerate(s):
        s[i] = v.split()
    
    s.sort(key=lambda x:len(x))

    for tup in s:
        for i in answer:
            tup.remove(i)
        answer.append(tup[0])
    
    answer = [int(i) for i in answer]
    
    return answer

"""
for tup in s:
    diff = set(tup) - set(answer)
    answer.append(list(diff)[0])
"""
