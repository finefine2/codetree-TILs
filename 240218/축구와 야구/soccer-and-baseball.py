# n = int(input())

# foot = []
# base = []

# for i in range(n):
#     s, b = map(int, input().split())
#     foot.append(s)
#     base.append(b)

# dp = [[0] * 12 for _ in range(10)]

# for i in range(n):
    
        
n = int(input())
abilities = []
for _ in range(n):
    s, b = map(int, input().split())
    abilities.append((s, b))

# 축구와 야구 능력 차이에 따라 정렬
abilities.sort(key=lambda x: abs(x[0] - x[1]), reverse=True)

# 축구팀과 야구팀을 선발
soccer_team = []
baseball_team = []
for s, b in abilities:
    if len(soccer_team) < 11:
        soccer_team.append(s)
    elif len(baseball_team) < 9:
        baseball_team.append(b)
    else:
        # 이미 축구팀과 야구팀이 꽉 찼으므로 남은 선수들 중 최대 능력치를 가진 팀에 배정
        if s > b and len(soccer_team) < 11:
            soccer_team.append(s)
        elif b >= s and len(baseball_team) < 9:
            baseball_team.append(b)

# 선발된 팀의 능력치 합계 계산
total_ability = sum(soccer_team) + sum(baseball_team)
print(total_ability)