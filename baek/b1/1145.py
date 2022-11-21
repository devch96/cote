a = sorted(list(map(int,input().split())))
n = a[0]
while True:
    count = 0
    for i in a:
        if n % i == 0:
            count += 1
    if count >= 3:
        break
    n+=1
print(n)