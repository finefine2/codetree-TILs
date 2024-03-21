# from sortedcontainers import SortedSet

# c, n = map(int, input().split())

# red = []
# for i in range(c):
#     a = int(input())
#     red.append(a)

# black = []
# for i in range(n):
#     a, b = map(int, input().split())
#     black.append((a, b))

# ans = 0
# red_sort = SortedSet(red)
# black.sort()

# for a, b in black:
#     idx = red_sort.bisect_left(a)
    
#     if idx != len(red_sort):
#         t = red_sort[idx]

#         if t <= b:
#             ans += 1
#             red_sort.remove(t)

# print(ans)


def max_pairs(C, N, red_stones, black_stones):
    red_stones.sort()  #
    black_stones.sort(key=lambda x: x[1])  
    pairs = 0
    j = 0  
    for red in red_stones:
        while j < N and black_stones[j][1] < red:  # 현재 검정 돌이 빨간 돌과 매칭되지 않는 경우 건너뛰기
            j += 1
        if j < N and black_stones[j][0] <= red <= black_stones[j][1]:  # 현재 빨간 돌과 매칭되는 검정 돌이 있는 경우
            pairs += 1
            j += 1  # 다음 검정 돌을 확인하기 위해 인덱스 증가
    return pairs

# 입력 받기
C, N = map(int, input().split())
red_stones = [int(input()) for _ in range(C)]
black_stones = [tuple(map(int, input().split())) for _ in range(N)]

# 최대 쌍 개수 출력
print(max_pairs(C, N, red_stones, black_stones))