a = input()
b = input()

c = sorted(a)
d = sorted(b)

s = "".join(c)
t = "".join(d)

if s == t:
    print("Yes")
else:
    print("No")