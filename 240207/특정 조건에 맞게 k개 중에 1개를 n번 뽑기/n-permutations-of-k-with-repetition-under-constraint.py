k, n = map(int, input().split())

arr = []

def arr_print():
    for k in arr:
        print(k, end = " ")
    print()

def choose(num):
    if num == n:
        arr_print()
        return
    
    for i in range(1, k+1):
        if len(arr) >= 2 and arr[-1] == i and arr[-2] == i:
            continue
        arr.append(i)
        choose(num + 1)
        arr.pop()


choose(0)