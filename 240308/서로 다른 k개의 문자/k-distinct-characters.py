st, k = map(str, input().split())

k = int(k)

str_idx = {}
left = 0
ans = 0

for right in range(len(st)):

    if st[right] in str_idx:
        str_idx[st[right]] += 1
    else:
        str_idx[st[right]] = 1
    
    while len(str_idx) > k:
        str_idx[st[right]] -= 1
        if str_idx[st[left]] == 0:
            del str_idx[st[left]]
        left += 1
    
    ans = max(ans, right - left + 1)
    

 
print(ans)




# left = 0
# str_idx = {}

# for right in range(len(st)):
#     if st[right] in str_idx and left <= str_idx[st[right]]:
#         left = str_idx[st[right]] + 1
#     else:
#         ans = max(ans, right - left + 1)

#     str_idx[st[right]] = right

# print(ans)