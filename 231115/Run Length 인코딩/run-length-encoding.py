A = input() 

ans = "" 

# 입력의 첫 값을 읽고 초기화 
curr_char = A[0] 
cnt = 1 

for target_char in A[1:]: 
    if target_char == curr_char: 
        # 지금까지 문자와 같으면 연속된 문자 개수만 추가해주고 넘어감 
        cnt += 1
    else: 
        # 지금까지 문자와 다르면 새로운 문자로 바꿈 
        # 지금까지 센 curr_char 와 cnt를 기록함 
        ans += curr_char 
        ans += str(cnt) 

        # curr_char와 cnt를 현재 값으로 초기화
        curr_char = target_char
        cnt = 1 
# 마지막 덩어리에 해당하는 curr_char와 cnt를 기록함 
ans += curr_char
ans += str(cnt) 

print(len(ans)) 
print(ans)