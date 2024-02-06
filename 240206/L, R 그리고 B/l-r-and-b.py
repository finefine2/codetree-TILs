arr = []
for i in range(10):
    tmp = list(input())
    arr.append(tmp)

lx, ly = 0, 0
bx, by = 0, 0
rx, ry = 0, 0
for i in range(10):
    for j in range(10):
        if arr[i][j] == 'L':
            lx = i
            ly = j
        elif arr[i][j] == 'R':
            rx = i
            ry = j
        elif arr[i][j] == 'B':
            bx = i
            by = j

ans = 0
if lx == bx:
    if rx == lx and ry > min(ly, by) and ry < max(ly, by):
        ans = abs(by - ly) + 1
    else:
        ans = abs(by - ly) - 1
elif ly == by:
    if ry == ly and rx > min(lx, bx) and rx < max(lx, bx):
        ans = abs(bx - lx) + 1
    else:
        ans = abs(bx - lx) - 1
else:
    ans = abs(bx - lx) + abs(by - ly) - 1

print(ans)