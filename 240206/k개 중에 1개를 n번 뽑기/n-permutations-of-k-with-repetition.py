k, n = map(int, input().split())

arr = []


def print_arr():
    for elem in arr:
        print(elem, end = " ")
    print()

def choose(num):
    if num == n:
        print_arr()
        return

    for i in range(1, k+1):
        arr.append(i)
        choose(num + 1)
        arr.pop()
    
    return


choose(0)