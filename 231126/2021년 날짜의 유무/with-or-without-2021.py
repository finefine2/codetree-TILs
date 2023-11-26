M,D = map(int,input().split())
'''
1  2  3  4  5  6  7  8  9  10  11  12
31 28 31 30 31 30 31 31 30 31  30  31

31: 1 3 5 7 8 10 12 
30: 4 6 9 11
28: 2

'''
def check_day(M,D): 
    if 1 <= M <= 12: 
        if M == 2:
            if D <= 28:
                return True 
        elif M == 4 or M == 6 or M == 9 or M == 11:
            if D <= 30: 
                return True 
        else:
            if D <= 31: 
                return True 

    return False

if check_day(): 
    print("Yes") 
else: 
    print("No")