def in_range(r,c):
    return 1 <= r <= N and 1 <= c <= N
N,M,P,C,D = map(int,input().split())
rudolf = tuple(map(int,input().split()))

board = [[0 for _ in range(N+1)] for _ in range(N+1)]
points = [0 for _ in range(P+1)]
is_live = [False for _ in range(P+1)]
pos = [(0,0) for _ in range(P+1)]
stun = [0 for _ in range(P+1)]

drs, dcs = [-1,0,1,0], [0,1,0,-1]

board[rudolf[0]][rudolf[1]] = -1

for _ in range(P):
    id, r, c = tuple(map(int,input().split()))
    pos[id] = (r, c)
    board[pos[id][0]][pos[id][1]] = id
    is_live[id] = True

for t in range(1, M+1):
    closeR, closeC, closeIdx = 10000, 10000, 0

    for i in range(1, P+1):
        if not is_live[i]:
            continue
        currBest = ((closeR - rudolf[0]) ** 2 + (closeC - rudolf[1]) ** 2, (-closeR, -closeC))
        currVal = ((pos[i][0] - rudolf[0]) ** 2 + (pos[i][1] -rudolf[1]) ** 2, (-pos[i][0], -pos[i][1]))

        if currVal < currBest:
            closeR, closeC = pos[i]
            closeIdx = i
    # 가까운 산타로 루돌프 움직임
    if closeIdx:
        prevRudolf = rudolf
        moveR = 0
        if closeR > rudolf[0]:
            moveR = 1
        elif closeR < rudolf[0]:
            moveR = -1

        moveC = 0
        if closeC > rudolf[1]:
            moveC = 1
        elif closeC < rudolf[1]:
            moveC = -1

        rudolf = (rudolf[0] + moveR, rudolf[1] + moveC)
        board[prevRudolf[0]][prevRudolf[1]] = 0
    if rudolf[0] == closeR and rudolf[1] == closeC:
        firstR = closeR + moveR * C
        firstC = closeC + moveC * C
        lastR, lastC = firstR, firstC

        stun[closeIdx] = t + 1

        while in_range(lastR, lastC) and board[lastR][lastC] > 0:
            lastR += moveR
            lastC += moveC

        while not (lastR == firstR and lastC == firstC):
            beforeR = lastR - moveR
            beforeC = lastC - moveC

            if not in_range(beforeR, beforeC):
                break
            idx = board[beforeR][beforeC]

            if not in_range(lastR, lastC):
                is_live[idx] = False
            else:
                board[lastR][lastC] = board[beforeR][beforeC]
                pos[idx] = (lastR, lastC)
            lastR, lastC = beforeR, beforeC
        points[closeIdx] += C
        pos[closeIdx] = (firstR, firstC)
        if in_range(firstR, firstC):
            board[firstR][firstC] = closeIdx
        else:
            is_live[closeIdx] = False
    board[rudolf[0]][rudolf[1]] = -1 
    
    for i in range(1, P+1): 
        if not is_live[i] or stun[i] >= t: 
            continue
        minDist = (pos[i][0] - rudolf[0]) ** 2 + (pos[i][1] - rudolf[1]) ** 2 
        moveDir = -1 
        
        for dir in range(4): 
            nr = pos[i][0] + drs[dir] 
            nc = pos[i][1] + dcs[dir] 
            
            if not in_range(nr,nc) or board[nr][nc] > 0: 
                continue
            dist = (nr - rudolf[0]) ** 2 + (nc - rudolf[1]) ** 2 
            if dist < minDist: 
                minDist = dist 
                moveDir = dir 
        
        if moveDir != -1:
            nr = pos[i][0] + drs[moveDir] 
            nc = pos[i][1] + dcs[moveDir] 
            if nr == rudolf[0] and nc == rudolf[1]: 
                stun[i] = t + 1 
                moveR = -drs[moveDir] 
                moveC = -dcs[moveDir] 
                
                firstR = nr + moveR * D 
                firstC = nc + moveC * D 
                lastR, lastC = firstR, firstC 
                
                if D == 1: 
                    points[i] += D 
                else: 
                    while in_range(lastR,lastC) and board[lastR][lastC] > 0: 
                        lastR += moveR
                        lastC += moveC
                    while lastR != firstR or lastC != firstC: 
                        beforeR = lastR - moveR
                        beforeC = lastC -moveC 
                        if not in_range(beforeR, beforeC): 
                            break 
                        idx = board[beforeR][beforeC] 
                        
                        if not in_range(lastR, lastC): 
                            is_live[idx] = False 
                        else: 
                            board[lastR][lastC] = board[beforeR][beforeC] 
                            pos[idx] = (lastR, lastC) 
                        lastR, lastC = beforeR, beforeC
                    points[i] += D 
                    board[pos[i][0]][pos[i][1]] = 0 
                    pos[i] = (firstR,firstC) 
                    if in_range(firstR, firstC): 
                        board[firstR][firstC] = i 
                    else: 
                        is_live[i] = False 
            else: 
                board[pos[i][0]][pos[i][1]] = 0
                pos[i] = (nr, nc) 
                board[nr][nc] = i 
    for i in range(1,P+1): 
        if is_live[i]: 
            points[i] += 1 
for i in  range(1,P+1): 
    print(points[i],end = " ")