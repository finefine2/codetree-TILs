n, m, k = map(int, input().split())
# 1번부터 m번까지
# k개의 말
# 나아가던 말이 m에 도달하면 1점
# n번의 턴

arr = list(map(int, input().split()))

yot = [1] * k
ans = []

def cal(yot):
    num = 0
    for i in range(k):
        if yot[i] >= m:
            num += 1
    
    return num

def move(now):
    if now == n:
        ans.append(cal(yot))
        return
    
    for i in range(k):
        yot[i] += arr[now]
        move(now + 1)
        yot[i] -= arr[now]

move(0)
print(max(ans))