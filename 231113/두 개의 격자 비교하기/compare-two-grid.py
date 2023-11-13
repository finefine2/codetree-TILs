n,m = map(int,input().split()) 
nums1 = [list(map(int,input().split())) for _ in range(n)] 
nums2 = [list(map(int,input().split())) for _ in range(n)] 

ans = [[0 for _ in range(m)] for _ in range(n)] 

for i in range(n): 
    for j in range(m): 
        if nums1[i][j] == nums2[i][j]: 
            ans[i][j] = 0 
        else: 
            ans[i][j] = 1 
for i in range(n): 
    for elem in ans[i]: 
        print(elem,end=" ")
    print()