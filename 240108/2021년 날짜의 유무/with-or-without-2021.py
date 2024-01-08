a, b = map(int, input().split())

def check(a, b):
    if a == 2:
        if b <= 28:
            return True
        else:
            return False
    if a == 1 or a == 3 or a == 5 or a == 7 or a == 8 or a == 10 or a == 12:
        if b <= 31:
            return True
        else:
            return False
    if a == 4 or a == 6 or a == 9 or a == 11:
        if b <= 30:
            return True
        else:
            return False

if check(a, b):
    print("Yes")
else:
    print("No")