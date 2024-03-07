st = input()

ans = 0

left = 0
str_idx = {}

for right in range(len(st)):
    if st[right] in str_idx and left <= str_idx[st[right]]:
        left = str_idx[st[right]] + 1
    else:
        ans = max(ans, right - left + 1)

    str_idx[st[right]] = right

print(ans)