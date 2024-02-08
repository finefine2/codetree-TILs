n = int(input())

arr = []
check = [0] * (n+1)

def choose(num):
    if num == n:
        for k in arr:
            print(k, end = " ")
        print()
        return

    for i in range(1, n+1):
        if check[i]:
            continue
        
        arr.append(i)
        check[i] = True
        choose(num + 1)
        arr.pop()
        check[i] = False

choose(0)