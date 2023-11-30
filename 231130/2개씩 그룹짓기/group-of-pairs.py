N = int(input()) 
nums = list(map(int,input().split())) 

# 부분집합은 원소가 2개이며 총 N개 쌍이 나오겠네 

if N == 1: 
    print(sum(nums))

else: 
    min_val = -1e9
    nums.sort()
    for i in range(N): 
        mid = nums[i] + nums[2*N-i-1]
        if mid > min_val:
            min_val = mid
    print(min_val)
'''
8 2 7 1 3 5
8 2 / 7 1 / 3 5

1 2 3 5 7 8 

1 8
2 7
3 5

2 3 5 5

1 5 3 7 5 6 10 4

1 3 4 5 5 6 7 10

'''