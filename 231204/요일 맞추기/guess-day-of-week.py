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

# 문제는 d1 이 0일 때 mon일수도 있고, 1일 때 mon일 수도 있다는 사실임 

def print_ans(d1,d2): 
    dates[d1] == "Mon"
    if d2 == d1-1: 
        print("Sun")
    elif d2 == d1: 
        print("Mon") 
    elif d2 == d1 + 1:
        print("Tue")
    elif d2 == d1 + 2:
        print("Wed")
    elif d2 == d1 + 3:
        print("Thu")
    elif d2 == d1 + 4:
        print("Fri")    
    elif d2 == d1 + 5:
        print("Sat")
day1 = count_num_days(m1,d1)
day2 = count_num_days(m2,d2)
print_ans(day1,day2)