nums = [] 


'''
0,0  0,1  0,2  0,3 
1,0  1,1  1,2  1,3
'''
for i in range(2): 
    nums.append(list(map(int,input().split()))) 

# 가로 평균 출력 
for i in range(2): 
    print(round(sum(nums[i]) / len(nums[0]),1),end=" ")
print() 
# 세로 평균 출력? 
print(round((nums[0][0] + nums[1][0])/2,1),end=" ")
print(round((nums[0][1] + nums[1][1])/2,1),end=" ")
print(round((nums[0][2] + nums[1][2])/2,1),end=" ")
print(round((nums[0][3] + nums[1][3])/2,1),end=" ")
print() 

print(round((nums[0][0] + nums[1][0] + nums[0][1] + nums[1][1] +nums[0][2] + nums[1][2] +nums[0][3] + nums[1][3])/8,1))