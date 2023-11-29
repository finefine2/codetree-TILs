N = int(input()) 
cnt = 0 
def get_count(n): 
    global cnt 
    if n == 1: 
        return cnt + 1
    if n % 2 != 0: 
        cnt += 1
        return get_count(n * 3 + 1)
    else: 
        cnt += 1
        return get_count(n // 2) 
    
print(get_count(N) -1 )