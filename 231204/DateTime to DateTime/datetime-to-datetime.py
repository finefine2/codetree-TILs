# start = 11일 11시 11분 
# a일 b시 c 분

a,b,c = map(int,input().split())

mins = 0 

def count_time(d,h,m): 
    # 일 = 24시 = 60 * 24 
    # 시 = * 60 
    # 분 = 분 
    return 60*24*d + 60 * h + m

if count_time(11,11,11) > count_time(a,b,c): 
    print(-1) 
else: 
    print(count_time(a,b,c) - count_time(11,11,11))