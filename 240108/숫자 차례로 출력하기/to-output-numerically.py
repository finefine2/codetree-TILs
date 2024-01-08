n = int(input())

def func1(n):
    if n == 0:
        return
    print(n, end = " ")
    func1(n-1)

def func2(n, m):
    if n == m+1:
        return
    print(n, end = " ")
    func2(n+1, m)

func2(1,n)
print()
func1(n)