arr = list(map(int, input().split()))

arr.sort()

abc = arr[-1]
a = abc - arr[-2]
c = arr[-3] - a
b = abc - a - c

print(a, b, c)


# a b c 
# ab ca bc abc