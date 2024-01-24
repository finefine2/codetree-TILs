n = int(input())

arr = []
for i in range(n):
    command = list(map(str, input().split()))
    a = command[0]
    if len(command) >= 2:
        b = command[1]
    if a == "push_back":
        arr.append(int(b))
    elif a == "pop_back":
        arr.pop()
    elif a == "size":
        print(len(arr))
    elif a == "get":
        print(arr[int(b)-1])