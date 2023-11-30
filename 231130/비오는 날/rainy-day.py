class weather: 
    def __init__(self,date,day,weat): 
        self.date = date 
        self.day = day 
        self.weat = weat 

n = int(input()) 
arr = [input().split() for _ in range(n)] 
weathers = [weather(date,day,weat) for date,day,weat in arr] 

target_idx = 0 
if weathers[target_idx].weat == "Rain": 
    print(weathers[target_idx].date, weathers[target_idx].day, weathers[target_idx].weat)
else: 
    for i in range(1,n+1): 
        if weathers[i].weat == "Rain": 
            target_idx = i 
            break 
    print(weathers[target_idx].date, weathers[target_idx].day, weathers[target_idx].weat)