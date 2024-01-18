n = int(input())
st = input()

ans = 0
for i in range(n):
    for j in range(1,n):
        cnt = 0
        for k in range(n):
            if st[k:k+j] == st[i:i+j]:
                cnt += 1
        if cnt >= 2:
            if ans < j:
                ans = j
            

        # if st.count(st[i:i+j]) >= 2:
        #     print(st[i:i+j])
        #     continue
        # else:
        #     if ans < j:
        #         ans = j
        #     break

print(ans+1)