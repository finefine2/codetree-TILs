n = int(input())

arr = []
for i in range(n):
    a, b = map(int, input().split())
    arr.append([a, b])

# arr.sort(key = lambda x: x[1])

Max = 0
def choose(line, i):
    global Max

    if len(line) > Max:
        Max = len(line)
    # Max보다 더 클 경우 갱신한다.
    
    if i >= n:
        return
    # n개를 선택한 경우 리턴한다.
    
    check = False
    for k in line:
        # 안겹칠 경우 check를 true로 하고 나간다.
        if (k[0] <= arr[i][0] and arr[i][0] <= k[1]) or (k[0] <= arr[i][1] and arr[i][1] <= k[1]) or (arr[i][0] < k[0] and arr[i][1] > k[1]):
            check = True
            break
    if not check:
        choose(line + [arr[i]], i+1)
    # check가 False일 경우 새로운 값을 넣어서 안으로 들어가준다.
    # check가 true가 될 경우 나온다.

    choose(line, i+1)
    # 그러면 원래의 line에 i를 늘려서 들어가게 된다.


choose([], 0)
print(Max)