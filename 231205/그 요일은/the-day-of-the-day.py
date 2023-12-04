# my solution - 살짝 복잡해보여도 맞췄지
# m1,d1,m2,d2 = map(int,input().split())
# A = input() 
# # 일단 요일들을 카운트하는 함수를 작성하자 
# def count_num_days(m,d): 
#     #       1  2  3  4  5  6 7 8 9 10 11 12
#     days=[0,31,29,31,30,31,30,31,31,30,31,30,31]
#     passed_days = 0 
#     # m-1 월까지는 전부 채움
#     for i in range(m): 
#         passed_days += days[i] 
#     passed_days += d

#     return passed_days
# # m1 d1 이 월욜
# # m2 d2 까지 일단 

# dates = ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
# # start 는 무조건 월요일
# start = count_num_days(m1,d1) 
# end = count_num_days(m2,d2) 

# start_idx = start % 7
# # 요일이 주어지면 인덱스를 찾자 
# def find_idx(s): 
#     idx = 0
#     if s == "Mon": 
#         idx = start_idx
#     elif s == "Tue": 
#         idx = start_idx+1    
#     elif s == "Wed": 
#         idx = start_idx+ 2 
#     elif s == "Thu":
#         idx = start_idx+ 3
#     elif s == "Fri":
#         idx = start_idx+ 4
#     elif s == "Sat":
#         idx = start_idx+ 5
#     elif s == "Sun":            
#         idx = start_idx+ 6
#     return idx
# def check_idx(i): 
#     if i >= 7:
#         i -= 7
#     return i 
# target_idx = 0 
# target_idx = check_idx(find_idx(A))

# ans = 0 
# for day in range(start,end+1): 
#     if day % 7 == target_idx: 
#         ans += 1 
# print(ans) 

# given solution 
m1,d1,m2,d2 = map(int,input().split()) 
A = input() 

def count_num_days(m,d): 
    days = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    total_days = 0 

    # 1 월부터 (m-1)월까지는 꽉 
    for i in range(1,m): 
        total_days += days[i] 

    # m 월은 d일만큼
    total_days += d 
    return total_days

def day_idx(s): 
    # 간단한 비교를 위해 요일을 숫자로 표기 
    if s == "Mon": 
        return 0
    elif s == "Tue": 
        return 1
    elif s == "Wed": 
        return 2
    elif s == "Thu": 
        return 3
    elif s == "Fri": 
        return 4
    elif s == "Sat": 
        return 5
    return 6

ans = 0
start = count_num_days(m1,d1) 
end = count_num_days(m2,d2) 
cur_day = day_idx("Mon") 

for date in range(start,end+1): 
    # 오늘 요일이 A 요일과 같다면 정답 추가 
    if cur_day == day_idx(A): 
        ans += 1 
    cur_day = (cur_day + 1) % 7 
print(ans)