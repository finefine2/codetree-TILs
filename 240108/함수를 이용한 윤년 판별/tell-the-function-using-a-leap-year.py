y = int(input())

def check(y):
    if y % 4 == 0:
        if y % 100 == 0:
            if y % 400 == 0:
                return True
            return False
        return True
    return False

if check(y):
    print("true")
else:
    print("false")