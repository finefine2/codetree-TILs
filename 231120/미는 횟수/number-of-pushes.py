A = input() 
B = input() 

cnt = 0 
# 문자열 A를 우측으로 한 칸씩 밀어보면서 비교 
for i in range(len(A)): 
    A = A[len(A)-1] + A[:len(A)-1]
    cnt += 1 

    # 문자열이 같을 경우 민 횟수를 출력 
    if A == B: 
        print(cnt) 
        break 
    
    if i == len(A) -1: 
        print(-1)