# # n, k = map(int, input().split())
# # arr = list(map(int, input().split()))

# # count = {}

# n, m = map(int, input().split())
# numbers = list(map(int, input().split()))

# counts = [0] * (m + 1)
# uniqueCount = 0  
# minLength = n + 1 

# start, end = 0, 0

# while end < n:
#     if counts[numbers[end]] == 0:
#         uniqueCount += 1
#     # 아직 없을 경우 늘려준다.
#     counts[numbers[end]] += 1
#     # 그리고 여기의 개수를 늘려준다.
    
#     # uniquecount가 m이고, end가 start보다 뒤일때
#     while uniqueCount == m and start <= end:
#         minLength = min(minLength, end - start + 1)
#         # 최소 길이 일 수 있으므로 해준다.
#         counts[numbers[start]] -= 1
#         if counts[numbers[start]] == 0:
#             uniqueCount -= 1
#         start += 1

#     end += 1

# # n보다 작응ㄹ 경우 그 길이를 출력해준다.
# if minLength < n:
#     print(minLength)
# else:
#     print(-1)


# 스트레스가 너무 받아서 그냥 답 코드를 구글링해서 놨다.

import math

INT_MAX = math.inf

n, m = map(int, input().split())
arr = [0] + list(map(int, input().split()))

count_array_in = [0] * (m + 1)
count_array_out = [0] * (m + 1)

distinct_num_in = 0
distinct_num_out = 0

def push(idx):
    global distinct_num_in, distinct_num_out
    num = arr[idx]

    if count_array_in[num] == 0:
        distinct_num_in += 1
    
    count_array_in[num] += 1

    count_array_out[num] -= 1

    if count_array_out[num] == 0:
        distinct_num_out -= 1

def pop(idx):
    global distinct_num_in, distinct_num_out
    num = arr[idx]

    count_array_in[num] -= 1
    if count_array_in[num] == 0:
        distinct_num_in -= 1
    
    if count_array_out[num] == 0:
        distinct_num_out += 1
    
    count_array_out[num] += 1

for i in range(1, n+1):
    if count_array_out[arr[i]] == 0:
        distinct_num_out += 1

    count_array_out[arr[i]] += 1

ans = INT_MAX

j = 0 
for i in range(1, n+1):
    while j + 1 <= n and distinct_num_in < m:
        push(j+1)
        j += 1

    if distinct_num_in < m:
        break

    if distinct_num_out == m:
        ans = min(ans, j - i + 1)

    pop(i)

if ans == INT_MAX:
    ans = -1

print(ans)