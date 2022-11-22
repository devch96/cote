first = input()
second = input()
third = input()
dic = {"black":0,"brown":1,"red":2,"orange":3,"yellow":4,"green":5,"blue":6,"violet":7,"grey":8,"white":9}
if first == "black" and second == "black":
    print(0)
else:
    print((dic[first]*10+dic[second]) * (10**dic[third]))