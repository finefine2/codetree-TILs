from collections import deque

def getInput():
    N, M = map(int, input().split())
    # 그래프를 받는 첫번째 방법
    graph = [list(map(str, input())) for _ in range(N)]

    # 그래프를 받는 두번째 방법
    # graph = []
    # for row in range(N):
    #     graph.append(list(map(str, input())))

    for row in range(N):
        for col in range(M):
            if graph[row][col] == 'R':
                Red = (row, col)
                graph[row][col] = '.'

            elif graph[row][col] == 'B':
                Blue = (row, col)
                graph[row][col] = '.'

    return N, M, graph, Red, Blue

def gravity(Red, Blue, direction):
    dx = [1, -1, 0, 0]  # 남북동서
    dy = [0, 0, 1, -1]
    check = 0  # 빨강들어가면 1, 파랑들어가면 2 더해줄거임.
    # 물론 check를 사용하지 않고 좌표값만 return해서 함수 바깥에서 비교하는 식으로 할 수도 있다.

    Rx, Ry = Red
    Bx, By = Blue

    Other = False # 다른 구슬이 있었는가?
    while True:
        Rnx, Rny = Rx+dx[direction], Ry+dy[direction]  # 범위 설정 안하나요? -> 상자라 벽이 무조건 감싸고있어서 괜찮다. 문제에 그렇게 가정해도 된다고 적혀있다.

        if graph[Rnx][Rny] == '.':
            if (Rnx, Rny) == Blue:
                Other = True
            Rx, Ry = Rnx, Rny
        elif graph[Rnx][Rny] == '#':
            if Other:  # 다른 구슬이 있었다면
                Rx, Ry = Rx-dx[direction], Ry-dy[direction]  # 그 전으로
                break
            else: break  # 아니라면 끝
        elif graph[Rnx][Rny] == 'O':
            check += 1
            break

        # 여기서 Red를 바꿔버리면, Blue를 검사할 때 Red가 또 발견된다. 그래서 나중에 해줄것이다.

    Other = False # 다른 구슬이 있었는가?
    while True:
        Bnx, Bny = Bx+dx[direction], By+dy[direction]

        if graph[Bnx][Bny] == '.':
            if (Bnx, Bny) == Red:
                Other = True
            Bx, By = Bnx, Bny
        elif graph[Bnx][Bny] == '#':
            if Other:  # 다른 구슬이 있었다면
                Bx, By = Bx-dx[direction], By-dy[direction]  # 그 전으로
                break
            else: break  # 아니라면 끝
        elif graph[Bnx][Bny] == 'O':
            check += 2
            break

    return (Rx, Ry), (Bx, By), check


# ===== 실제 실행하는 부분 =====

N, M, graph, Red, Blue = getInput()
queue = deque([(Red, Blue, 0)])

flag = False
while queue:
    r, b, turn = queue.popleft()
    if turn == 10: continue

    for i in range(4):
        nr, nb, check = gravity(r, b, i)
        if check == 0: queue.append((nr, nb, turn+1))
        elif check == 1:
            print(turn+1)
            flag = True
            break
    if flag: break
else:
    print(-1)