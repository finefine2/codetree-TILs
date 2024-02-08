n = int(input())

arr = []

three = [4, 5, 6]



def find(arr):
    cnt = 1
    while True:
        a1, b1 = len(arr) - cnt, len(arr) - 1
        a2, b2 = a1 - cnt, a1 - 1

        # a1 < cnt가 되도 break
        if a2 < 0:
            break
        
        # (cnt, 1) 구간과 (a1 - cnt, a1 - 1)의 구간이 같을 경우 False
        # 이 값들은 cnt가 늘어나면서 바뀐다.
        if arr[a1 : b1 + 1] == arr[a2 : b2 + 1]:
            return False
        cnt += 1
    return True

def choose(num):
    if num == n:
        for k in arr:
            print(k, end = "")
        # print(''.join(arr))
        quit()
    
    for i in range(3):
        arr.append(three[i])
        if find(arr):
            choose(num + 1)
        arr.pop()



choose(0)