# n, k = map(int, input().split())
# arr = list(map(int, input().split()))

# count = {}

n, m = map(int, input().split())
numbers = list(map(int, input().split()))

counts = [0] * (m + 1)
uniqueCount = 0  
minLength = n + 1 

start, end = 0, 0

while end < n:
    if counts[numbers[end]] == 0:
        uniqueCount += 1
    # 아직 없을 경우 늘려준다.
    counts[numbers[end]] += 1
    # 그리고 여기의 개수를 늘려준다.
    
    # uniquecount가 m이고, end가 start보다 뒤일때
    while uniqueCount == m and start <= end:
        minLength = min(minLength, end - start + 1)
        # 최소 길이 일 수 있으므로 해준다.
        counts[numbers[start]] -= 1
        if counts[numbers[start]] == 0:
            uniqueCount -= 1
        start += 1

    end += 1

# n보다 작응ㄹ 경우 그 길이를 출력해준다.
if minLength <= n:
    print(minLength)
else:
    print(-1)