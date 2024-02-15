st = input()

arr = []
flag = False
for k in st:
    if k == '(':
        arr.append('(')
    elif k == ')':
        if arr:
            arr.pop()
        else:
            flag = True

if flag or len(arr) >= 1:
    print("No")
else:
    print("Yes")