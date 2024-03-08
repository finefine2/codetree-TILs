st, k = map(str, input().split())

k = int(k)

str_idx = {}
left = 0
ans = 0

for right in range(len(st)):
    if st[right] not in str_idx:
        str_idx[st[right]] = 1
    else:
        str_idx[st[right]] += 1
    
    while len(str_idx) > k:
        str_idx[st[left]] -= 1
        if str_idx[st[left]] == 0:
            del str_idx[st[left]]
        left += 1
    
    ans = max(ans, right - left + 1)
    

        # right_char = s[right]
        # if right_char not in char_frequency:
        #     char_frequency[right_char] = 0
        # char_frequency[right_char] += 1

        # # 서로 다른 문자의 수가 k를 초과하는 경우 왼쪽 포인터 이동
        # while len(char_frequency) > k:
        #     left_char = s[left]
        #     char_frequency[left_char] -= 1
        #     if char_frequency[left_char] == 0:
        #         del char_frequency[left_char]
        #     left += 1
        
        # # 현재 윈도우의 길이가 최대 길이보다 큰지 검사
        # max_length = max(max_length, right - left + 1)

 
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