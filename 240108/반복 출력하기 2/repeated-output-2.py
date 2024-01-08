n = int(input())

def func(n):
    if n == 0:
        return
    
    print("HelloWorld")
    func(n-1)

func(n)