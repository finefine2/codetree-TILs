# 처음, 마지막 포인트를 제외한 나머지 포인트를 순서대로 건너뛰었을 때 거리 계산
N = int(input()) 
arr = [list(map(int,input().split())) for _ in range(N)] 

ans = 1e9 

for i in range(1,N-1): 
    dist = 0 
    prev_idx = 0 
    for j in range(1,N): 
        if i == j: 
            continue 
        dist += abs(arr[prev_idx][0] - arr[j][0]) + abs(arr[prev_idx][1]-arr[j][1]) 
        prev_idx = j 
    ans = min(ans,dist) 
print(ans)