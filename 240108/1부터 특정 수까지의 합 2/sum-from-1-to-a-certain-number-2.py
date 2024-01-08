n = int(input())

s = 0
def func(n):
    if n == 0:
        return
    global s
    s += n
    func(n-1)

func(n)

print(s)