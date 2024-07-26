n = int(input())

st = input()
target = input()

ans = 0
check = False
cnt = 0
for i in range(n):
    if st[i] != target[i]:
        if not check:
            check = True
            ans += 1
            cnt = 1
            # 처음에는 1개로 시작
        else:
            # 1을 더해주고 만약에 cnt가 4가 넘으면 ans를 늘려주고 cnt를 초기화
            cnt += 1
            if cnt > 4:
                ans += 1
                cnt = 1
    else:
        check = False
        cnt = 0

print(ans)