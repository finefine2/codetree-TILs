# my solution is much better than given one
N = int(input()) 
nums = [int(input()) for _ in range(N)] 
def carry(a,b,c): 
    max_len = max(len(str(a)), len(str(b)), len(str(c)))
    cnt = 0 
    while a > 0 or b > 0 or c > 0: 
        if (a % 10 + b % 10 + c % 10) >= 10: 
            break 
        elif (a % 10 + b % 10 + c % 10) < 10: 
            a //= 10 
            b //= 10 
            c //= 10
            cnt += 1
    if cnt == max_len: 
        return True 
    else: 
        return False

ans = -1
# 완탐 돌리기 
for i in range(N): 
    for j in range(i+1,N):
        for k in range(j+1,N): 
            if carry(nums[i],nums[j],nums[k]): 
                ans = max(ans, nums[i] + nums[j] + nums[k])
print(ans) 

# given solution 
# 일의 자리, 십의 자리, 백의 자리, 천의 자리를 각각 더 해보기 
# 왜냐면 input 조건이 10000 미만이기떄문
# 변수 선언 및 입력
# n = int(input())
# arr = [
# 	int(input())
# 	for _ in range(n)
# ]

# # 모든 쌍을 다 잡아봅니다.
# ans = -1
# for i in range(n):
# 	for j in range(i + 1, n):
# 		for k in range(j + 1, n):
# 			carry = False
			
# 			# 일의 자리에서 carry가 발생하는 경우
# 			if arr[i] % 10 + arr[j] % 10 + arr[k] % 10 >= 10:
# 				carry = True
			
# 			# 십의 자리에서 carry가 발생하는 경우
# 			if arr[i] % 100 // 10 + arr[j] % 100 // 10 + arr[k] % 100 // 10 >= 10:
# 				carry = True
			
# 			# 백의 자리에서 carry가 발생하는 경우
# 			if arr[i] % 1000 // 100 + arr[j] % 1000 // 100 + arr[k] % 1000 // 100 >= 10:
# 				carry = True
			
# 			# 천의 자리에서 carry가 발생하는 경우
# 			if arr[i] % 10000 // 1000 + arr[j] % 10000 // 1000 + arr[k] % 10000 // 1000 >= 10:
# 				carry = True
			
# 			if carry == False:
# 				ans = max(ans, arr[i] + arr[j] + arr[k]);

# print(ans)