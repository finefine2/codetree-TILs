n = int(input())

arr = list(map(int, input().split()))

def get_digit(num, pos):
    return (num // 10**pos) % 10

def radix_sort(arr, k):
    for pos in range(k):
        arr_new = [list() for _ in range(10)]
        
        for i in range(len(arr)):
            digit = get_digit(arr[i], pos)
            arr_new[digit].append(arr[i])

        store_arr = []
        for i in range(10):
            store_arr.extend(arr_new[i])

        arr = store_arr

    return arr

ans = radix_sort(arr, len(str(max(arr))))
print(*ans)