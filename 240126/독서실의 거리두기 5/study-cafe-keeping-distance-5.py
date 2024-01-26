# pair_sum = [9,5,10] 

# def is_equal_arr(arr1,arr2): 
#     arr1.sort() 
#     arr2.sort() 
#     if len(arr1) != len(arr2): 
#         return False 
#     for elem1, elem2 in zip(arr1, arr2): 
#         if elem1 != elem2: 
#             return False 
#     return True 

# for a in range(1,11): 
#     for b in range(a,11): 
#         for c in range(b,11): 
#             if is_equal_arr([a+b,b+c,c+a],pair_sum): 
#                 print(a,b,c) 
N = int(input()) 
s_in = input() 
s_list = []
for s in s_in: 
    s_list.append(int(s))

ans = 0 

def count(arr): 
    dist = 1e9 
    for i in range(len(arr)): 
        for j in range(len(arr)): 
            if i == j: 
                continue 
            if arr[i] == 1 and arr[j] == 1: 
                dist = min(dist,abs(i-j)) 
    return dist 

ans = -1e9 
for i in range(N): 
    if s_list[i] == 0: 
        s_list[i] = 1 
        dist = count(s_list)
        ans = max(ans,dist) 
        s_list[i] = 0 
print(ans)