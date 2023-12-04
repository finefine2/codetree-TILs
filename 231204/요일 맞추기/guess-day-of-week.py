day_list = [0,31,28,31,30,31,30,31,31,30,31,30,31]
dates= ["Sun","Mon","Tue","Wed","Thu","Fri","Sat"]

# monday_start = 1월 3일 --> 3 
# if days % 7 == 3 -> monday 
# 3 4 5 6 0 1 2 
# m t w t f s s 

# 요일은 매주 반복되어 돌아온다
m1,d1,m2,d2 = map(int,input().split())
def count_num_days(m,d):
    passed_days = 0

    for i in range(m): 

        passed_days += day_list[i]

    return (passed_days + d) % 7 

def print_ans(d1,d2): 
    cnt_day = d1-d2
    if cnt_day == 0: 
        print("Mon")
    elif cnt_day == 1: 
        print("Sun")
    elif cnt_day == 2: 
        print("Sat")
    elif cnt_day == 3: 
        print("Fri")
    elif cnt_day == 4: 
        print("Thu")
    elif cnt_day == -1: 
        print("Wed")
    elif cnt_day == -2: 
        print("Tue")

day1 = count_num_days(m1,d1)
day2 = count_num_days(m2,d2)
print_ans(day1,day2)