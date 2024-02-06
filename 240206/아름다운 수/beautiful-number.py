n = int(input())
arr = []
ans = 0

# 1 2 3 4
# 해당 숫자만큼 연속으로

def beauty():
    i = 0
    while i < n:

        if i + arr[i] - 1 >= n:
            return False
        # i에 i만큼 더 했을때 n보다 크면 False

        for j in range(i, i + arr[i]):
            if arr[j] != arr[i]:
                return False
        # i 부터 arr[i]를 더한 만큼 즉, 그 숫자 개수 만큼 수들에서 하나라도 다르면 False
        
        i += arr[i]

    return True


def find(num):
    global ans
    if num == n:
        if beauty():
            ans += 1
        return
    
    for i in range(1, 5):
        arr.append(i)
        find(num + 1)
        arr.pop()

    

find(0)
print(ans)