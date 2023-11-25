n = int(input()) 

def leap_year(n): 
    # 4의 배수가 아니면 윤년이 아님 
    if n % 4 != 0: 
        return False 

    # 여기까지 온 이상 4의 배수로 가정 
    # 그 중 100의 배수가 아니면 윤년
    if n % 100 != 0: 
        return True 

    # 여기까지 온 이상 100의 배수로 가정 
    # 그 중 400의 배수면 윤년 
    if n % 400 == 0:
        return True 
    
    # 여기까지 온 이상 100의 배수지만, 400의 배수가 아님 
    # 따라서 윤년이 아님 
    return False 

if leap_year(n): 
    print("true") 
else:
    print("false")