N = int(input()) 

nums = list(map(int,input().split())) 
# a 인덱스까지 중 가장 큰 값을 리턴 
def get_max(a):
    if a == 0: 
        return nums[0] 
    return max(get_max(a-1), nums[a]) 
print(get_max(N-1))