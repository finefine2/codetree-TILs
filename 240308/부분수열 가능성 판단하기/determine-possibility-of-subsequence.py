n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))


def is_subsequence(a, b, n, m):
    i = 0  
    j = 0  

    # A와 B를 순회하며 B의 모든 요소가 A에 순서대로 있는지 확인
    while i < n and j < m:
        if a[i] == b[j]:
            j += 1
        i += 1

    # B의 모든 요소가 A에서 찾아졌는지 여부를 반환
    return j == m

ans = 0

for k in range(len(b)):
    c = b[:k] + b[k+1:]

    if is_subsequence(a, c, n, m-1):
        ans += 1

print(ans)