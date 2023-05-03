T = int(input())
for test_case in range(1, T+1):
    ymd = input()
    year = ymd[:4]
    month = ymd[4:6]
    day = ymd[6:]
    flag = False
    if int(month) in [1,3,5,7,8,10,12]:
        if 1<=int(day)<=31:
            flag = True
    elif int(month) == 2:
        if 1<=int(day)<=28:
            flag = True
    elif int(month) in [4,6,9,11]:
        if 1<=int(day)<=30:
            flag = True
    if flag:
        print(f'#{test_case} {year}/{month}/{day}')
    else:
        print(f'#{test_case} -1')
