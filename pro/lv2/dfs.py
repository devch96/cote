def solution(numbers, target):
    count=[0]
    def DFS(i,j,k):
        if i == len(k):
            if j == target:
                count[0] += 1
            return
        v = k[i]
        DFS(i+1, j+v, k)
        DFS(i+1, j-v, k)
    DFS(0,0,numbers)
    return count[0]

"""
    count = 0
    que = [[0,0]]

    while que:
        index, process = que.pop()

        if len(numbers) > index:
            que.append([index+1, process+numbers[index]])
            que.append([index+1, process-numbers[index]\)
        
        if len(numbers) == index:
            if process == target:
                count += 1
    return count
"""