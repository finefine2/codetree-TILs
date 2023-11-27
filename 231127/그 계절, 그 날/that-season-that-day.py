Y,M,D = map(int,input().split()) 
'''
31: 1 3 5 7 8 10 12 
30: 4 6 9 11
28: 2 

'''
# 1. 윤년여부를 체크한다 

def leap_year(y): 
    # 4의 배수가 아니면 윤년이 아님 
    if y % 4 != 0: 
        return False 

    # 여기까지 온 이상 4의 배수로 가정 
    # 그 중 100의 배수가 아니면 윤년
    if y % 100 != 0: 
        return True 

    # 여기까지 온 이상 100의 배수로 가정 
    # 그 중 400의 배수면 윤년 
    if y % 400 == 0:
        return True 
    
    # 여기까지 온 이상 100의 배수지만, 400의 배수가 아님 
    # 따라서 윤년이 아님 
    return False 

# 2. M월 D일이 존재하는지 확인한다 
# my solution 
# def check_day(y,m,d): 
#     if leap_year(y): # 2월은 29일
#         if m == 2: 
#             if d <= 29: 
#                 return True 
#         elif m == 4 or m == 6 or m == 9 or m == 11: 
#             if d <= 30: 
#                 return True
#         else: 
#             if d <= 31: 
#                 return True 
#     else: # 윤년이면 2월은 28일까지 
#         if m == 2: 
#             if d <= 28: 
#                 return True 
#         elif m == 4 or m == 6 or m == 9 or m == 11: 
#             if d <= 30: 
#                 return True 
#         else: 
#             if d <= 31: 
#                 return True 
#     return False

# # 계절을 출력한다 
# def season(m): 
#     ans = ""
#     if 3 <= m <= 5: 
#         ans = "Spring"
#     elif 6 <= m <= 8: 
#         ans = "Summer" 
#     elif 9 <= m <= 11: 
#         ans = "Fall"
#     else: 
#         ans = "Winter" 
#     return ans 


# if check_day(Y,M,D): 
#     print(season(M)) 
# else: 
#     print(-1)

# given solution 
def exist_day(y,m,d): 
    #                  1. 2.  3. 4.  5    6.  7.  8.  9. 10. 11  12   
    num_of_days = [0, 31, 0, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    # 윤년 확인 
    num_of_days[2] = 29 if leap_year(y) else 28 
    # d 가 해당 월의 최대 일 수를 넘지 않아야 함 
    return d <= num_of_days[m] 

# y년 m월 d일이 존재 하지 않으면 -1 
if not exist_day(Y,M,D): 
    print(-1) 
else: 
    if 3 <= M <= 5: 
        print("Spring") 
    elif 6 <= M <= 8: 
        print("Summer") 
    elif 9 <= M <= 11: 
        print("Fall") 
    else: 
        print("Winter")