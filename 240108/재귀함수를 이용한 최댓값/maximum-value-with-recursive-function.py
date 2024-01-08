n = int(input())

arr = list(map(int, input().split()))

k = arr[0]
def f(n):
    if n == 0:
        return
    global arr
    global k
    if k < arr[n-1]:
        k = arr[n-1]
    f(n-1)

f(n)
print(k)