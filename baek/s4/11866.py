n,k = map(int,input().split())
lt = [i for i in range(1, n+1)]
print("<", end='')
i = 0
while lt:
    i += k-1
    if i >= len(lt):
        i = i%len(lt)
    print(lt.pop(i), end='')
    if lt:
        print(',', end=' ')
print(">")