n, m = map(int, input().split())

arr = []


def choose(num, last):
    if num == m + 1:
        for k in arr:
            print(k, end = " ")
        print()
        return
    
    for i in range(last, n+1):
        arr.append(i)
        choose(num + 1, i + 1)
        arr.pop()

choose(1, 1)