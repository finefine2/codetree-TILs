a, b, c = map(str, input().split())

if b == '+':
    print(f"{a} + {c} = {int(a) + int(c)}")
elif b == '-':
    print(f"{a} - {c} = {int(a) - int(c)}")
elif b == '/':
    print(f"{a} / {c} = {int(a) // int(c)}")
elif b == '*':
    print(f"{a} * {c} = {int(a) * int(c)}")
else:
    print("False")