'''
tmp 초기화
아래에서 위로 올라오며 비어있지 않을 때만 tmp 채우기 
tmp를 다시 arr로 복사 
'''
# for 2-d arr 
# BLANK = 0 
# n = 10 
# arr = [[0] * n for _ in range(n)] 
# tmp = [[0] * n for _ in range(n)] 

# for row in range(n-1,-1,-1): 
#     tmp[row][col] = BLANK

# tmp_row = n-1 
# for row in range(n-1,-1,-1): 
#     if arr[row][col] != BLANK: 
#         tmp[tmp_row][col] = arr[row][col] 
#         tmp_row -= 1 

# for row in range(n): 
#     arr[row][col] = tmp[row][col]

# for 1-d arr
# BLANK = 0 
# end_of_arr = 0 
# arr = [0] * 6 
# tmp = [0] * 6 
# end_of_tmp = 0 

# for i in range(end_of_arr): 
#     if arr[i] != BLANK: 
#         tmp[end_of_tmp] = arr[i] 
#         end_of_tmp += 1 

# for i in range(end_of_tmp): 
#     arr[i] = tmp[i] 

# end_of_arr = end_of_tmp

n = int(input()) 

tower = [int(input()) for _ in range(n)] 
s1,e1 = map(int,input().split()) 
s2,e2 = map(int,input().split()) 


def remove(s,e,arr): 
    tmp = [0] * len(arr) 
    if s == e: 
        for i in range(len(arr)): 
            if i != s - 1: 
                tmp[i] = arr[i] 
            else: 
                continue
    else: 
        for i in range(len(arr)): 
            if i < s-1: 
                tmp[i] = arr[i] 
            elif i > e-1: 
                tmp[i] = arr[i] 
            else: 
                continue 
    return tmp 

def clean(arr): 
    ans = [] 
    for a in arr: 
        if a != 0: 
            ans.append(a) 
    return ans

mid = clean(remove(s1,e1,tower))
ans = clean(remove(s2,e2,mid))
if len(ans) == 0: 
    print(0) 
else: 
    print(len(ans))
    for a in ans: 
        print(a)