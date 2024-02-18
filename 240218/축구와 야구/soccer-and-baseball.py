# n = int(input())

# foot = []
# base = []

# for i in range(n):
#     s, b = map(int, input().split())
#     foot.append(s)
#     base.append(b)

# dp = [[0] * 12 for _ in range(10)]

# for i in range(n):
    
        
def maximize_ability(n, abilities):
    # 각 학생의 축구와 야구 능력치를 따로 저장하는 리스트
    foot = [ability[0] for ability in abilities]
    base = [ability[1] for ability in abilities]

    # 축구팀과 야구팀의 인원수 상한은 각각 11명, 9명이므로 이를 초과하지 않도록 설정
    max_football_players = min(11, n)
    max_baseball_players = min(9, n)

    # DP 배열 초기화
    # dp[i][j][k]: i번째 학생까지 고려하고, 축구팀에 j명, 야구팀에 k명을 선택했을 때의 최대 능력치 합
    dp = [[[-1] * (max_baseball_players + 1) for _ in range(max_football_players + 1)] for _ in range(n + 1)]

    # DP를 통해 최대 능력치 합 구하기
    def dp_maximize_ability(idx, football_players, baseball_players):
        if idx == n:
            return 0
        if dp[idx][football_players][baseball_players] != -1:
            return dp[idx][football_players][baseball_players]

        # 현재 학생을 축구팀에 추가하는 경우
        football_option = 0
        if football_players < max_football_players:
            football_option = foot[idx] + dp_maximize_ability(idx + 1, football_players + 1, baseball_players)

        # 현재 학생을 야구팀에 추가하는 경우
        baseball_option = 0
        if baseball_players < max_baseball_players:
            baseball_option = base[idx] + dp_maximize_ability(idx + 1, football_players, baseball_players + 1)

        # 현재 학생을 어느 팀에도 추가하지 않는 경우
        no_selection_option = dp_maximize_ability(idx + 1, football_players, baseball_players)

        # 세 경우 중 최대값을 DP 배열에 저장
        dp[idx][football_players][baseball_players] = max(football_option, baseball_option, no_selection_option)

        return dp[idx][football_players][baseball_players]

    # 최대 능력치 합 반환
    return dp_maximize_ability(0, 0, 0)


n = int(input())
abilities = []
for _ in range(n):
    s, b = map(int, input().split())
    abilities.append((s, b))

result = maximize_ability(n, abilities)
print(result)