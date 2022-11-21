str = input()
temp = []
for x in range(1, len(str)-1):
    for y in range(x+1, len(str)):
        a = str[:x][::-1]
        b = str[x:y][::-1]
        c = str[y:][::-1]
        temp.append(a+b+c)
print(min(temp))
            