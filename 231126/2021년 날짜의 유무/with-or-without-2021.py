# my solution 

# M,D = map(int,input().split())
# '''
# 1  2  3  4  5  6  7  8  9  10  11  12
# 31 28 31 30 31 30 31 31 30 31  30  31

# 31: 1 3 5 7 8 10 12 
# 30: 4 6 9 11
# 28: 2

# '''
# def check_day(M,D): 
#     if 1 <= M <= 12: 
#         if M == 2:
#             if D <= 28:
#                 return True 
#         elif M == 4 or M == 6 or M == 9 or M == 11:
#             if D <= 30: 
#                 return True 
#         else:
#             if D <= 31: 
#                 return True 

#     return False

# if check_day(M,D): 
#     print("Yes") 
# else: 
#     print("No") 

# given sol 
m,d = map(int,input().split()) 

# 윤년이 아닐 때 m번째 달의 마지막 날을 반환하는 함수를 작성 
def last_day_num(m): 
    if m == 2: 
        return 28 
    if m == 4 or m == 6 or m == 9 or m == 11: 
        return 30 
    return 31 

# 윤년이 아닐 때 m월 d일이 존재하는지 여부를 확인 
def check_day(m,d): 
    if m <= 12 and d <= last_day_num(m): 
        return True 
    return False 

if check_day(m,d): 
    print("Yes") 
else: 
    print("No")