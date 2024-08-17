from itertools import combinations

N = int(input())
P = [list(map(int,input().split())) for _ in range(N)] 
def calculate_strength(P, tasks):
    strength = 0
    for i in range(len(tasks)):
        for j in range(i + 1, len(tasks)):
            strength += P[tasks[i]][tasks[j]] + P[tasks[j]][tasks[i]]
    return strength

def gen_combi(arr, n):
    result = []
    if n == 0:
        return [[]]

    for i in range(0, len(arr)):
        elem = arr[i]
        for C in gen_combi(arr[i + 1:], n - 1):
            result.append([elem] + C)
            
    return result

def min_strength_difference(n, P):
    tasks = list(range(n))
    half_n = n // 2
    min_difference = float('inf')

    for morning_tasks in gen_combi(tasks, half_n):
        evening_tasks = [task for task in tasks if task not in morning_tasks]
        
        morning_strength = calculate_strength(P, morning_tasks)
        evening_strength = calculate_strength(P, evening_tasks)
        
        difference = abs(morning_strength - evening_strength)
        min_difference = min(min_difference, difference)

    return min_difference
print(min_strength_difference(N,P))