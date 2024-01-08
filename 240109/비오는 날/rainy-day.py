class data:
    def __init__(self, day, date, weath):
        self.day = day
        self.date = date
        self.weath = weath
    
n = int(input())

info = []
for _ in range(n):
    day, date, weath = tuple(map(str, input().split()))
    info.append(data(day, date, weath))

Min = 9999999999
Mindate = ""
Maxday = ""
Maxweath = ""
for i in range(n):
    if info[i].weath == 'Rain':
        a, b, c = info[i].day.split('-')
        s = int(a+b+c)
        if s < Min:
            Min = s
            Mindate = info[i].date
            Minday = info[i].day
            Minweath = info[i].weath

print(f"{Minday} {Mindate} {Minweath}")