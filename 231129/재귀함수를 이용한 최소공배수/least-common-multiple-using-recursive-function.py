# my solution 

# N = int(input()) 
# nums = list(map(int,input().split())) 

# def gcd(n1,n2): 
#     if n2 == 0: 
#         return n1 
#     return gcd(n2, n1 % n2)

# def lcm(n1,n2): 
#     return (n1 * n2) // gcd(n1,n2) 
# if N == 1: 
#     print(nums[0]) 
# else: 
#     ans = lcm(nums[0],nums[1]) 
#     for i in range(1,len(nums)-1): 
#         ans = lcm(ans,nums[i+1])
#     print(ans)

'''
given solution 
모든 원소에 대해 n번째 원소부터 첫 원소까지 비교하며 최소공배수를 구해 그 값을 return 
'''
# 변수 선언 및 입력:
n = int(input())
arr = [0] + list(map(int, input().split()))


# 두 수간의 최소공배수를 구하여 반환합니다.
def lcm(a, b):
    gcd = 1
    for i in range(1, min(a, b) + 1):
        if a % i == 0 and b % i == 0:
            gcd = i

    return a * b // gcd


# index번째 까지 인덱스의 숫자 중에 가장 큰 값을 반환합니다.
def get_lcm_all(index):
    # 남은 원소가 1개라면 그 자신이 답이 됩니다.
    if index == 1:
        return arr[1]

    # 1번째 ~ index - 1번째 원소의 최소공배수를 구한 결과와
    # 현재 index 원소의 최소공배수를 구하여 반환합니다.
    return lcm(get_lcm_all(index - 1), arr[index])

   
# 모든 수의 최소공배수를 구합니다.
print(get_lcm_all(n))