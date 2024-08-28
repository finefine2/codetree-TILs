def is_happy_sequence(sequence, m):
    count = 1  # 연속된 원소의 개수를 세기 위한 변수
    for i in range(1, len(sequence)):
        if sequence[i] == sequence[i - 1]:
            count += 1
            if count >= m:  # 연속된 원소가 m개 이상이면 행복한 수열
                return True
        else:
            count = 1  # 다른 원소가 나오면 카운트 초기화
    return False

def count_happy_sequences(grid, m):
    n = len(grid)
    happy_count = 0
    
    # 각 행 검사
    for row in grid:
        if is_happy_sequence(row, m):
            happy_count += 1
    
    # 각 열 검사
    for col in range(n):
        column_sequence = [grid[row][col] for row in range(n)]
        if is_happy_sequence(column_sequence, m):
            happy_count += 1
    
    return happy_count

# 입력 예시
N,M = tuple(map(int,input().split()))
board = [list(map(int,input().split())) for _ in range(N)]
# 결과 출력
result = count_happy_sequences(board, M)
print(result)  # 행복한 수열의 총 개수 출력