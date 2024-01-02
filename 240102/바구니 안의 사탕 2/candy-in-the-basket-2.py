N, K = map(int,input().split()) 
placed = [0] * 100

for _ in range(N): 
    c, p = map(int,input().split()) 
    # 여러 바구니가 한 지점에 있을 수 있음
    placed[p-1] += c 
ans = -5000

# 구간 설정 함수 
for i in range(100):
    start = max(0,i-K) 
    end = min(100,i+K+1)
    ans = max(ans,sum(placed[start:end]))
print(ans)