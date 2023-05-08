T = int(input())
for test_case in range(1,T+1):
    len = int(input())
    numList = list(map(int,input().split()))
    cnt = 0
    for i in range(1,len-1):
        if numList[i] not in [max(numList[i-1],numList[i],numList[i+1]), min(numList[i-1], numList[i], numList[i+1])]:
            cnt += 1
    print(f'#{test_case} {cnt}')