n = int(input()) 

class Forecast: 
    def __init__(self,date,day,weather): 
        self.date, self.day, self.weather = date, day, weather

ans = Forecast("9999-99-99","","")
for _ in range(n): 
    date, day, weather = input().split()

    f = Forecast(date,day,weather) 
    if weather == "Rain": 
        if ans.date >= f.date: 
            ans = f 
print(ans.date,ans.day,ans.weather)