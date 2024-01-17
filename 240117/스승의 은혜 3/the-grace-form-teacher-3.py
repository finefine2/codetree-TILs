n, b = map(int, input().split())


arr = []
for i in range(n):
    p, s = map(int, input().split())
    arr.append((p, s))

# arr.sort(lambda x : x[0] + x[1])

ans = 0
for i in range(n):
    price = [0] * n
    
    for j in range(n):
        price[j] = arr[j][0] + arr[j][1]
    price[i] = arr[i][0]//2 + arr[i][1]

    price.sort()

    # i = 0
    num = 0
    s = 0

    for j in range(n):
        if price[j] + s > b:
            break

        s += price[j]
        num += 1

    ans = max(ans, num)
    # while True:
    #     s += arr[i][0]
    #     s += arr[i][1]
    
    #     if s > b:
    #         if s - (arr[i][0] * 0.5) <= b:
    #             num += 1
    #             break
    #         else:
    #             break
    #     i += 1
    #     num += 1

print(ans)