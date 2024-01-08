a = input()
s = set()

def func(a):
    for i in a:
        s.add(i)

func(a)
if len(s) >= 2:
    print("Yes")
else:
    print("No")