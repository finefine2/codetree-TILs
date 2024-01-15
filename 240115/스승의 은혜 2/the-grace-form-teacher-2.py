N,B = map(int,input().split()) 
prices = [int(input()) for _ in range(N)] 
ans = 0 
# 학생 하나에 쿠폰 쓸 때 선물 가능한 학생의 최대 명수 
for i in range(N): 
    # i번째에 쿠폰 쓸 때 선물 가능한 학생 수 구하기 
    # tmp 배열을 만들어 i번째 학생에 쿠폰 쓸 때 각 학생의 선물 가격 저장 
    tmp = [prices[j] for j in range(N)] 
    tmp[i] /= 2 
    # 가격 순 정렬 
    # 가격이 낮은 순으로 사줄 때 많이 줄 수 있음 
    tmp.sort() 
    student, cnt = 0, 0
    # 가장 많은 학생에게 줄 때, 학생 수는? 
    for j in range(N): 
        if cnt + tmp[j] > B: 
            break 
        cnt += tmp[j] 
        student += 1 
    ans = max(ans,student) 
print(ans)