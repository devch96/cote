def fact(n):
    a = 1
    for i in range(1,n+1):
        a *= i
    return a
n = int(input())
cnt = 0
for x in str(fact(n))[::-1]:
    if x != '0':
        break
    else:
        cnt += 1
print(cnt)