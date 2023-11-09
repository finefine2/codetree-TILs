# 변수 선언 및 입력:

n = int(input())
nums = list(map(int, input().split()))

# 최댓값 찾기
max_num = -1

for n in nums:
    # 최대가 될 수 있는 후보입니다.
    if max_num < n:
        # 갱신할 수 있는지 확인하기 위해 이 숫자의 등장 빈도를 셉니다.
        count = 0
        for elem in nums:
            if elem == n:
                count += 1
        
        # 이 숫자가 배열에서 유일할때만 갱신합니다.
        if count == 1:
            max_num = n

print(max_num)