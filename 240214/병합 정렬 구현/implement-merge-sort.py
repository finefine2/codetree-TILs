N = int(input()) 
nums = list(map(int,input().split()))
merged_nums = [0] * N 

def merge(low,mid,high): 
    i,j = low, mid + 1 
    k = low 
    while i <= mid and j <= high: 
        if nums[i] <= nums[j]: 
            merged_nums[k] = nums[i] 
            k += 1 
            i += 1 
        else: 
            merged_nums[k] = nums[j] 
            k += 1 
            j += 1 
    while i <= mid: 
        merged_nums[k] = nums[i] 
        k += 1 
        i += 1 
    while j <= high: 
        merged_nums[k] = nums[j]
        k += 1 
        j += 1 
    for k in range(low,high+1): 
        nums[k] = merged_nums[k] 
def merge_sort(low,high): 
    if low < high: 
        mid = (low + high) // 2 
        merge_sort(low,mid) 
        merge_sort(mid+1, high) 
        merge(low,mid,high) 
merge_sort(0,N-1) 
for n in nums: 
    print(n,end=" ")