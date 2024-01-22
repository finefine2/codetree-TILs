n, m, p = map(int, input().split())

arr = []
for i in range(m):
    c, u = map(str, input().split())
    arr.append((c, u))
    # if dict[c] < int(u):
    #     dict[c] = int(u)
    
for i in range(n):
    num = chr(ord('A') + i)
    flag = False
    for c, u in arr:
        if int(u) >= int(arr[p-1][1]) and c == num:
            flag = True

    if not flag:
        print(num, end = " ")



# 누가 들어오면 이전의 모든 메세지를 읽게 된다.
# 총 m개의 메세지 중 p번째 메세지를 읽지 않았을 가능성이 있는 사람 출력