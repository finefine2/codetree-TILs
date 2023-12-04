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
'''
m t w t f s s 
0 1 2 3 4 5 6
1 2 3 4 5 6 0
2 3 4 5 6 0 1
3 4 5 6 0 1 2
4 5 6 0 1 2 3
5 6 0 1 2 3 4
6 0 1 2 3 4 5

-0 1 2 3 4 5 6         0
 0 1 2 3 4 5 -1        1
 0 1 2 3 4 -2 -1       2
 0 1 2 3 -3 -2 -1      3
 0 1 2 -4 -3 -2 -1    4
 0 1 -5 -4 -3 -2 -1
 0 -6 -5 -4 -3 -2 -1
'''
def print_ans(d1,d2): 
    if d2 - d1 == 0: 
        print("Mon")
    elif d2 - d1 == 1 or d2 - d1 == -6: 
        print("Tue")
    elif d2 - d1 == 2 or d2 - d1 == -5: 
        print("Wed")
    elif d2 - d1 == 3 or d2 - d1 == -4: 
        print("Thu")
    elif d2 - d1 == 4 or d2 - d1 == -3: 
        print("Fri")
    elif d2 - d1 == 5 or d2 - d1 == -2: 
        print("Sat")
    elif d2 - d1 == 6 or d2 - d1 == -1: 
        print("Sun")
day1 = count_num_days(m1,d1)
day2 = count_num_days(m2,d2)
print_ans(day1,day2)