from collections import deque

n = int(input())

# 거꾸로 풀면 되었던 듯
# 사실 근데 이거 DP로 풀면 금방인데 BFS 단원이므로 BFS로 풀어보자

plus = [1, -1, 2, 3]
check = [0] * (2 * n + 1)
arr = [0] * (2 * n + 1)

q = deque()

def isin(num):
    return 1 <= num < 2*n + 1

def BFS():
    q.append(1)
    check[1] = True

    while q:
        x = q.popleft()
        for i in range(4):
            if i == 0 or i == 1:
                nx = x + plus[i]
            else:
                nx = x * plus[i]
        
            if isin(nx) and not check[nx]:
                check[nx] = 1
                arr[nx] = arr[x] + 1
                q.append(nx)
            
            if nx == n:
                print(arr[nx])
                return

BFS()