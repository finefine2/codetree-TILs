nums1 = [list(map(int,input().split())) for _ in range(3)]
input()
nums2 = [list(map(int,input().split())) for _ in range(3)] 

ans = [[0 for _ in range(3)] for _ in range(3)]


for i in range(3): 
    for j in range(3): 
        ans[i][j] = nums1[i][j] * nums2[i][j] 

for i in range(3): 
    for a in ans[i]: 
        print(a,end=" ")
    print()