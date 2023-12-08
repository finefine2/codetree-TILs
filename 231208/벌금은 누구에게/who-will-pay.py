N,M,K = map(int,input().split()) 
students = [i for i in range(1,N+1)] 
count_num = [0] * (1+N)
nums = [int(input()) for _ in range(M)] 


'''
N명 학생: 5 
M개 벌칙: 7 
K 이상: 3 
students = [1,2,3,4,5]
count_num = [0,0,0,0,0,0]
nums = [2,5,2,3,5,2,4]

'''

ans = -1 
for i in range(M):
    target = nums[i] 
    count_num[target] += 1 
    if count_num[target] == K: 
        ans = target
        break 
print(ans)