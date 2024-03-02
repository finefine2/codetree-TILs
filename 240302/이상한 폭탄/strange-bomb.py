n, k = map(int, input().split())

arr = []
for i in range(n):
    a = int(input())
    arr.append(a)

last_pos = dict()
Max_explode = -1

for i, bomb_num in enumerate(arr):
    if bomb_num in last_pos and i - last_pos[bomb_num] <= k:
        Max_explode = max(Max_explode, bomb_num)
    # last_pos에 bomb_num이 있을때 -> 즉 그 번호가 있었을 경우
    # 그리고 그 거리가 k이하일때
    # Max를 재준다.
    
    last_pos[bomb_num] = i
    # last_pos에 이 폭탄 번호 딕셔너리에 i를 넣는다.


print(Max_explode)