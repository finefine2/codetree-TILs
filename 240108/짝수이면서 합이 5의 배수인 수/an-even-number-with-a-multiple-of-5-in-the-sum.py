n = int(input())

def check(n):
    return n % 2 == 0 and (n % 10 + n // 10) % 5 == 0
    
if check(n):
    print("Yes")
else:
    print("No")