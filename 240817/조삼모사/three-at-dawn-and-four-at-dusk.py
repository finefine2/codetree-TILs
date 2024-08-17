# 아침 조합을 구한다 
# 저녁 조합을 구한다 
# 둘 간의 차를 구한다 

N = int(input()) 
board = [list(map(int,input().split())) for _ in range(N)] 


def gen_combi(arr,n): 
    result = []

    if n == 0: 
        return [[]]

    for i in range(0,len(arr)): 
        elem = arr[i] 
        for C in gen_combi(arr[i+1:], n-1): 
            result.append([elem]+C) 
    return result

def calculate_ans(numbers, board): 
    ans = 0 

    for i in range(len(numbers)): 
        for j in range(i+1,len(numbers)): 
            ans += board[numbers[i]][numbers[j]] + board[numbers[j]][numbers[i]]

    return ans 

numbers = list(range(N))
morning_numbers = gen_combi(numbers,N//2) 
evening_numbers = [num for num in numbers if num not in morning_numbers]

min_diff = 1e9 
for morning_num in morning_numbers: 
    evening_num = [num for num in numbers if num not in morning_num] 
    
    morning_sum = calculate_ans(morning_num,board) 
    evening_sum = calculate_ans(evening_num,board)

    min_diff = min(min_diff, abs(morning_sum-evening_sum))
print(min_diff)