n = int(input())

def func(n):
    if n == 0:
        return
    print(n, end = " ")
    func(n-1)
    print(n, end = " ")

func(n)