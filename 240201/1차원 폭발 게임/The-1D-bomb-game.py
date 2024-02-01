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
for _ in range(n):
    arr.append(int(input()))

while True:
    i = 0
    same = []  # 제거할 폭탄의 인덱스를 저장하는 리스트
    while i < len(arr):
        cnt = 1
        while i + cnt < len(arr) and arr[i] == arr[i + cnt]:
            cnt += 1
        
        if cnt >= m:
            # M개 이상 연속되면 해당 인덱스 범위 추가
            for j in range(i, i + cnt):
                same.append(j)

        i += cnt

    if not same:
        # 더 이상 제거할 폭탄이 없으면 종료
        break

    # 제거할 폭탄을 제외하고 리스트 다시 구성
    arr = [arr[i] for i in range(len(arr)) if i not in same]

# 결과 출력
print(len(arr))
for bomb in arr:
    print(bomb)