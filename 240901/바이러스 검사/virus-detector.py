# 검사팀장과 검사팀원
# 한가게당 팀장은 한명, 팀원은 여러명 가능
# 가게당 팀장 한 명은 무조건 필요

n = int(input())
client = map(int, input().split())
lead, member = map(int, input().split())

ans = 0
for k in client:
    c = k
    if c - lead >= 0:
        ans += 1
        c -= lead

        if c % member == 0 and c // member != 0:
            ans += (c // member)
        elif c % member != 0:
            ans += (c // member) + 1
    else:
        ans += 1

print(ans)