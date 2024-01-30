n, m, q = map(int, input().split())

arr = []
for i in range(n):
    st = list(map(int, input().split()))
    arr.append(st)


def move(prev, now):
    for i in range(m):
        if arr[prev][i] == arr[now][i]:
            return True
    return False
# prev행과 now행에 대하여 하나라도 같으면 바로 True를 리턴한다.

def wind(prev, now, dir):
    if now < 0 or now >= n or not move(prev, now):
        return
    # now 자체가 범위를 넘거나 move가 False인 경우 return 해서 스탑한다.
    
    if dir == "L":
        arr[now] = arr[now][1:] + [arr[now][0]]
        dir = "R"
        # L일 경우 1부터 끝까지에다가 맨 처음 부분을 리스트로 만들어서 더해주면 L
    else:
        arr[now] = [arr[now][-1]] + arr[now][:-1]
        dir = "L"
        # R일 경우 맨 마지막 부분을 리스트로 만들어서 맨 마지막을 뺀 나머지를 뒤에 더해준다.
    
    # prev가 더 클 경우에는 위로 가는 걸 진행
    if now < prev:
        wind(now, now - 1, dir)
    else:
        wind(now, now + 1, dir)
    # 아닐 때는 밑으로 가는 것을 진행


for i in range(q):
    r, d = map(str, input().split())
    r = int(r) - 1

    if d == "L":
        arr[r] = [arr[r][-1]] + arr[r][:-1]
    else:
        arr[r] = arr[r][1:] + [arr[r][0]]
    
    wind(r, r-1, d)
    wind(r, r+1, d)
    # 여기에서 위로 아래로 가는 것을 진행한다.

for k in arr:
    print(*k)

# for i in range(n):
#     for j in range(m):
#         print(arr[i][j], end = " ")
#     print()