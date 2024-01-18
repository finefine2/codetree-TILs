# cnt = 0 
# for i in range(100,1000): 
#     d1,d2,d3 = tuple(map(int,list(str(i)))) 
#     if d1 + d2 == d3 or d1 + d3 == d2 or d2 + d3 == d1: 
#         cnt += 1 
# print(cnt) 

X,Y = map(int,input().split()) 
ans = -1e9 
def get_num(n): 
    ans = 0
    n_list = list(str(n)) 
    for n in n_list: 
        ans += int(n) 
    return ans

for i in range(X,Y+1): 
    tmp = get_num(i)
    ans = max(ans,tmp)
print(ans)