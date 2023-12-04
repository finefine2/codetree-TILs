class Number: 
    def __init__(self,number,index): 
        self.number, self.index = number, index
N = int(input())
nums = []
arr = list(map(int,input().split())) 
nums = [Number(num,i) for i,num in enumerate(arr)]

ans = [0] * N 

nums.sort(key = lambda x: (x.number, x.index)) 
# 정렬된 숫자들의 원래 인덱스를 활용한 정답 배열 
for i, n in enumerate(nums): 
    ans[n.index] = i + 1 # 인덱스 수정 
 
for i in range(N):
    print(ans[i],end=" ")