from datetime import datetime
month, day, year, hour, minute = map(str,input().replace(',','').replace(":"," ").split(" "))
mon = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
dic = {mon[i]:i+1 for i in range(len(mon))}
now = datetime(int(year),dic[month],int(day),int(hour),int(minute))
new = datetime(int(year)+1,1,1,0,0)
last = datetime(int(year),1,1,0,0)
result = 100 - (((new-now).total_seconds()/(new-last).total_seconds())*100)
print(result)