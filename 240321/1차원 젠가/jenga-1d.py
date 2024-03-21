'''
tmp 초기화
아래에서 위로 올라오며 비어있지 않을 때만 tmp 채우기 
tmp를 다시 arr로 복사 
'''
# n = int(input()) 

# tower = [int(input()) for _ in range(n)] 
# s1,e1 = map(int,input().split()) 
# s2,e2 = map(int,input().split()) 

# def remove(s,e,arr): 
#     tmp = [0] * len(arr) 
#     if s == e: 
#         for i in range(len(arr)): 
#             if i != s - 1: 
#                 tmp[i] = arr[i] 
#             else: 
#                 continue
#     else: 
#         for i in range(len(arr)): 
#             if i < s-1: 
#                 tmp[i] = arr[i] 
#             elif i > e-1: 
#                 tmp[i] = arr[i] 
#             else: 
#                 continue 
#     return tmp 

# def clean(arr): 
#     ans = [] 
#     for a in arr: 
#         if a != 0: 
#             ans.append(a) 
#     return ans

# mid = clean(remove(s1,e1,tower))
# ans = clean(remove(s2,e2,mid))
# if len(ans) == 0: 
#     print(0) 
# else: 
#     print(len(ans))
#     for a in ans: 
#         print(a)

# solution 2
# tmp를 이용, [s,e] 밖의 원소들만 tmp에 옮겨준 뒤, 다시 arr로 복사하는 작업
# n = int(input()) 
# numbers = [int(input()) for _ in range(n)] 

# end_of_arr = n 
# def cut_arr(start,end):
#     global end_of_arr, numbers 

#     tmp = [] 
#     for i in range(end_of_arr): 
#         if i < start or i > end: 
#             tmp.append(numbers[i]) 
#     end_of_arr = len(tmp) 
#     for i in range(end_of_arr): 
#         numbers[i] = tmp[i] 
# for _ in range(2): 
#     s,e = map(int,input().split()) 

#     cut_arr(s-1,e-1) 

# print(end_of_arr)
# for i in range(end_of_arr): 
#     print(numbers[i]) 

# solution 3 
n = int(input()) 
numbers = [int(input()) for _ in range(n)] 
end_of_arr = n 

def cut_arr(start, end): 
    global end_of_arr
    cut_len = end - start + 1
    for i in range(end+1, end_of_arr): 
        numbers[i-cut_len] = numbers[i] 
    end_of_arr -= cut_len 

for _ in range(2): 
    s,e = map(int,input().split()) 
    cut_arr(s-1,e-1) 

print(end_of_arr) 
for i in range(end_of_arr): 
    print(numbers[i])