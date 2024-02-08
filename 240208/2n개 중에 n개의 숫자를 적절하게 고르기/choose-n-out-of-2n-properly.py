# n = int(input())

# arr = list(map(int, input().split()))

# arr1 = []
# arr2 = []
# import sys
# Min = sys.maxsize

# def cal(arr1):
#     for k in arr:
#         if k not in arr1:
#             arr2.append(k)

#     return abs(sum(arr1) - sum(arr2))


# def choose(num):
#     global Min

#     if num == n:
#         Min = min(Min, cal(arr1))
#         return Min

#     for i in range(2 * n):
#         arr1.append(arr[i])
#         choose(num + 1)
#         arr1.pop()


# print(choose(0))

import sys
n = int(input())
arr = list(map(int, input().split()))

Min = sys.maxsize

def cal_diff(arr1, arr2):
    return abs(sum(arr1) - sum(arr2))

def choose(num, arr1, arr2):
    global Min

    if len(arr1) > n or len(arr2) > n:  
        return
        
    if num == 2 * n:
        if len(arr1) == n and len(arr2) == n:  
            diff = cal_diff(arr1, arr2)
            Min = min(Min, diff)

        return

    choose(num + 1, arr1 + [arr[num]], arr2)
    choose(num + 1, arr1, arr2 + [arr[num]])

choose(0, [], []) 
print(Min)