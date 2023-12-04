# hours, mins = 2,5 
# passed_time = 0 

# while True: 
#     if hours == 4 and mins == 1: 
#         break 

#     passed_time += 1
#     mins += 1 

#     if mins == 60: 
#         hours += 1 
#         mins = 0 
# print(passed_time)


a,b,c,d = map(int,input().split()) 

# a 시 b 분 ~ c시 d분 

hours, mins = a,b 
ans = 0
while True: 
    if hours == c and mins == d: 
        break 
    ans +=1
    mins += 1 
    
    if mins == 60: 
        hours += 1 
        mins =0 
print(ans)