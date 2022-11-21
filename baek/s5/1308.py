import datetime
y1,m1,d1 = map(int,input().split())
y2,m2,d2 = map(int,input().split())
d = int(str(datetime.date(y2,m2,d2)-datetime.date(y1,m1,d1)).split()[0])
over = 0 
for i in range(0,1000) :
    if i%400==0 :
        over +=366
    elif i%100==0 :
        over += 365
    elif i%4==0 :
        over += 366
    else :
        over += 365
if d >= over:
    print('gg')
else:
    print(f'D-{d}')