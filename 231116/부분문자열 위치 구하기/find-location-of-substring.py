import sys

input_str = input() #부분 문자열
target_str = input() #목적 문자열

input_len, target_len = len(input_str), len(target_str)# 각 문자열의 길이를 저장


for i in range(input_len):#각 입력 문자열은 시작점으로 잡아야하기에 입력 문자열의 길이만큼 반복
#입력 문자열 i가 정해졌을 때 남은 문자열의 길이가 입력 문자열보다 작을 경우 탐색할 이유 x
#시작점 + 탐색이 성립하기 위한 최소 길이(목적 문자열) - 시작점 찾은 수 >= 입력 문자열
    if i + target_len - 1 >= input_len:
        continue
    # 매칭 유무
    is_matched = True
    for j in range(target_len):
        if input_str[i + j] != target_str[j]:#i가 시작점일 시 목적 문자열의 크기만큼 반복하여 맞는 것이 있는지 찾는다.
            is_matched = False #일치하는 것이 없으면 실패
    
    if is_matched:
        print(i)
        sys.exit(0)


print(-1)