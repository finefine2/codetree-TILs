# my solution 
# n = int(input()) 
# nums = list(map(int,input().split()))
# def find_mid(a): 
#     a.sort() 
#     return a[len(a)//2]

# for i in range(1, len(nums)+1, 2):
#     sub_num = nums[:i] 
#     print(find_mid(sub_num),end=" ")

# given solution 
N = int(input()) 
nums = list(map(int,input().split())) 
# 홀수번째 수를 지날때마다 정렬하고 중앙값 출력
for i in range(N): 
    if i % 2 == 0: 
        # 오름차순 정렬 
        sorted_nums = sorted(nums[:i+1]) 
        print(sorted_nums[i//2],end=" ")