n,m = map(int,input().split())

'''
0 1 2 3 --- n + m - 1 
'''

nums = [[0 for _ in range(m)] for _ in range(n)]
start = 1 
cnt = 0

while start < n * m +1:
    for i in range(n): 
        for j in range(m): 
            if (i+j) == cnt: 
                nums[i][j] = start 
                start += 1 
    cnt += 1
for i in range(n): 
    for j in range(m): 
        print(nums[i][j],end=" ") 
    print()