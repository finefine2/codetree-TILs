n = int(input())

def func(n):
    if n == 0:
        return
    func(n-1)
    print("*" * n)


func(n)