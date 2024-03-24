N, M = map(int,input().split()) 
bombs = list(int(input()) for _ in range(N)) 

def get_end_idx(start_idx, curr_num): 
    for end_idx in range(start_idx+1,len(bombs)): 
        if bombs[end_idx] != curr_num: 
            return end_idx - 1 
    return len(bombs) - 1 

while True: 
    explode = False 

    for curr_idx, num in enumerate(bombs): 
        if num == 0:
            continue 
        end_idx = get_end_idx(curr_idx,num) 
        if end_idx - curr_idx +1 >= M: 
            bombs[curr_idx:end_idx+1] = [0] * (end_idx - curr_idx +1)
            explode = True 
    bombs = list(filter(lambda x: x>0, bombs))
    if not explode: 
        break 
print(len(bombs))
for b in bombs: 
    print(b)