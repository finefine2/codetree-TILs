n, m = map(int, input().split())

arr = []
for i in range(m):
    a, b = map(int, input().split())
    arr.append([b, a - 1])

select_arr = []
ans = m
arr.sort()

def ladder():
    arr1 = [i for i in range(n)]
    arr2 = [i for i in range(n)]
    # 시작하는 숫자를 정의

    for k, idx in arr:
        arr1[idx], arr1[idx + 1] = arr1[idx + 1], arr1[idx]
    for k, idx in select_arr:
        arr2[idx], arr2[idx + 1] = arr2[idx + 1], arr2[idx]
    # arr와 selected_arr에 대해서 각각 idx와 idx+1의 인덱스를 가진 수들을 바꾸어준다.

    for i in range(n):
        if arr1[i] != arr2[i]:
            return False
        # 하나라도 다르다면 False
    
    return True
    # 모두 같을 경우 True

def find_line(num):
    global ans

    if num == m:
        if ladder():  # True일 경우 선택한 배열의 수의 min을 구해준다.
            ans = min(ans, len(select_arr))
        return
    
    # 선택된 배열에 arr[num]을 계속 넣어준다.
    select_arr.append(arr[num])
    find_line(num + 1)
    select_arr.pop()
    # num을 하나 늘려가며 찾아준다.
    # 그리고 하나씩 pop하고

    # 다시 들어간다.
    find_line(num + 1)


find_line(0)
print(ans)