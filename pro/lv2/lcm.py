def solution(arr):
    answer = arr[0]
    def GCD(x,y):
        while y:
            x, y = y , x%y
        return x

    def LCM(x,y):
        return x*y // GCD(x,y)

    for i in arr:
        answer = LCM(answer,i)

    return answer
