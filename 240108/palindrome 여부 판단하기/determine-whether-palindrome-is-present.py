a = input()

def palin(s):
    if s == s[::-1]:
        return True
    return False

if palin(a):
    print("Yes")
else:
    print("No")