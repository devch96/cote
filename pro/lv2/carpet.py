def solution(brown, yellow):
    size = brown + yellow
    width = 0
    vertical = 0
    for i in range(2,size):
        width = i
        vertical = ((brown+4) // 2) - i
        if width*vertical == size:
            return sorted([width,vertical], reverse = True)
    
