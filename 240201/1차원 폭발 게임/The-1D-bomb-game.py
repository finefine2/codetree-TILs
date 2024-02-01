# n, m = map(int, input().split())

# arr = []
# for i in range(n):
#     a = int(input())
#     arr.append(a)


# while True:

#     arr2 = []
#     samecheck = False
#     lastcheck = False
#     for i in range(len(arr)-1):
#         if arr[i] == arr[i+1]:
#             if i + 1 == len(arr) - 1:
#                 lastcheck = True
#                 samecheck = True
#         else:
#             arr2.append(arr[i])
#     if not lastcheck:
#         arr2.append(arr[len(arr) - 1])
    
#     if not samecheck:
#         break

#     arr = arr2

# print(len(arr))
# for k in arr:
#     print(k) 

n, m = map(int, input().split())

arr = []
for i in range(n):
    a = int(input())
    arr.append(a)

while True:
    arr2 = []
    i = 0
    while i < len(arr) - 1:
        if arr[i] == arr[i + 1]:
            # 연속된 같은 숫자를 건너뛰기
            while i < len(arr) - 1 and arr[i] == arr[i + 1]:
                i += 1
        else:
            arr2.append(arr[i])
        i += 1

    # 마지막 원소 처리
    if len(arr) >= 1:
        if not (i < len(arr) and arr[i] == arr[i - 1]):
            arr2.append(arr[-1])

    if len(arr2) == len(arr):
        # 더 이상 제거할 연속된 숫자가 없으면 반복 종료
        break
    arr = arr2

print(len(arr))
for k in arr:
    print(k)