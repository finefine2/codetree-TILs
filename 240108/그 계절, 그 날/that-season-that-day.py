a, b, c = map(int, input().split())

def check(a, b, c):
    if a == 2 and yoon(c):
        if b <= 29:
            return True
        else:
            return False
    if a == 2 and not yoon(c):
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

def season(a, b):
    if a == 3 or a == 4 or a == 5:
        return "Spring"
    elif a == 6 or a == 7 or a == 8:
        return 'Summer'
    elif a == 9 or a == 10 or a == 11:
        return 'Fall'
    else:
        return 'Winter'

def yoon(a):
    if a % 4 == 0:
        if a % 100 == 0:
            if a % 400 == 0:
                return True
            return False
        return True

if check(b, c, a):
    print(season(b, c))
else:
    print(-1)