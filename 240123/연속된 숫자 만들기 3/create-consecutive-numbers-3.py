a, b, c = map(int, input().split())


ans = 0
if a + 1 == b and b + 1 == c:
    ans = 0
else:
    ans = max(c - b - 1, b - a - 1)
# 거리를 한칸씩 좁혀가면서 이동하는 방식이 결국 최대이므로 
# 최대 이동횟수는 중간의 간격 중 제일 큰 간격 - 1이 된다.

print(ans)