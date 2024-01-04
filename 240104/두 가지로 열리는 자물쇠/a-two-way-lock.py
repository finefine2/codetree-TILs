# 각 자리에 들어갈 숫자를 일일이 카운팅하며 입력으로 주어진 숫자들과 전부 차이가 2인지 확인
N = int(input())
a1,b1,c1 = map(int,input().split()) 
a2,b2,c2 = map(int,input().split()) 
def calc_dist(num,a): 
    return abs(num-a) <= 2 or abs(num-a) >= N-2
cnt = 0 
for i in range(1,N+1): 
    for j in range(1,N+1): 
        for k in range(1,N+1): 
            if calc_dist(i,a1) and calc_dist(j,b1) and calc_dist(k,c1): 
                cnt += 1 
            elif calc_dist(i,a2) and calc_dist(j,b2) and calc_dist(k,c2): 
                cnt += 1 
print(cnt)