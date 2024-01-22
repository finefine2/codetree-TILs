n, l = map(int, input().split())

arr = list(map(int, input().split()))

# H 이상인 숫자의 수가 H개 이상인 것
# 그것을 만족하는 H 중 최대값

# 여기에서는 최대 L개의 원소 값을 1씩 올려 H 점수를 최대로 만들고자 한다.

# 내림차순을 한 뒤에 인덱스  만큼 보다 값이 작으면 그 전에 끝


ans = 0

# i는 즉 각각의 h를 뜻한다.
for i in range(101):
    cnt = 0

    for j in range(n):
        if arr[j] < i:
            continue
        cnt += 1
        # arr[j]가 i보다 작아질때까지 세준다.
    
    # L은 어차피 서로 다른 원소의 값을 1씩만 올릴 수 있으므로 이렇게 1 더해서 체크해주면 된다.
    if l>0:
        if cnt >= i+1:
            ans = max(i+1, ans)
    else:
        if cnt >= i:
            ans = max(i, ans)

print(ans)