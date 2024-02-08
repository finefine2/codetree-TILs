n, m = map(int, input().split())

arr = list(map(int, input().split()))
# xor = []

# ans = 0

# def XOR(arr):
#     res = 0
#     for k in arr:
#         res = res ^ k
    
#     return res
    

# def choose(num, last):
#     global ans
#     if num == m+1:
#         x = XOR(arr)
#         ans = max(ans, x)
#         return
    
#     for i in range(last, len(arr)):
#         xor.append(arr[i])
#         choose(num + 1, last + 1)
#         xor.pop()
    

# choose(1, 1)
# print(ans)

Max = 0
def XOR(n, m, arr, xor):
    global Max

    if m == 0:
        Max = max(xor, Max)
        
    for i in range(0, len(arr)):
        XOR(n, m-1, arr[i+1:], xor ^ arr[i])

XOR(n, m, arr, 0)
print(Max)