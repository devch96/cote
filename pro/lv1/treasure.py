def solution(n, arr1, arr2):
    answer = []
    arr1 = [["#" if x == "1" else " " for x in format(i,"0"+str(n)+"b")] for i in arr1]
    arr2 = [["#" if x == "1" else " " for x in format(i,"0"+str(n)+"b")] for i in arr2]
    for a1, a2 in zip(arr1, arr2):
        temp = ''
        for i in range(n):
            if a1[i] =="#" or  a2[i] == "#":
                temp += "#"
            else:
                temp += " "
        answer.append(temp)
    return answer

print(solution(5,[9,20,28,18,11],[30,1,21,17,28]))
"""
bin(arr1|arr2)
"""
