n = int(input()) 
nums = list(map(int,input().split()))
def find_mid(a): 
    a.sort() 
    return a[len(a)//2]

for i in range(1, len(nums)+1, 2):
    sub_num = nums[:i] 
    print(find_mid(sub_num),end=" ")