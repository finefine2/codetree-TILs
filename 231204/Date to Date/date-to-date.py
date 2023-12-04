# my solu
# m1, d1, m2, d2 = map(int,input().split())
# ans = 0 
# num_of_days = [31,28,31,30,31,30,31,31,30,31,30,31]

# while True: 
#     if m1 == m2 and d1 == d2: 
#         break 
#     ans += 1 
#     d1 += 1 

#     if d1 > num_of_days[m1-1]: 
#         m1 += 1
#         d1 = 1
# print(ans+1)    

# given sol
m1,d1,m2,d2 = map(int,input().split())

def num_of_days(m,d): 
    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    total_days = 0
    for i in range(m-1): 
        total_days += days[i]
    total_days += d 

    return total_days

total_days = num_of_days(m2,d2) - num_of_days(m1,d1) +1
print(total_days)