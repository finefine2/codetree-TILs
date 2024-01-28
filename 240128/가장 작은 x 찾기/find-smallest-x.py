# n 7= int(input())

# arr = []
# for i in range(n):
#     a, b = map(int, input().split())
#     arr.append((a, b))

# ans = 0
# for i in range(1, 10001):
#     cnt = 0
#     for j in range(n):
#         if arr[j][0] <= (2 ** (j+1)) * i <= arr[j][1]:
#             cnt += 1
#     if cnt == n:
#         ans = i
#         break

# print(ans)
MAX_NUM = 10000

N = int(input()) 
conditions = [list(map(int,input().split())) for _ in range(N)] 
# x 가능한지    
def satisfy(num): 
    for a,b in conditions: 
        num *= 2 
        if num < a or num > b: 
            return False 
    return True 

for x in range(1,MAX_NUM+1): 
    if satisfy(x): 
        print(x) 
        break