# from functools import cmp_to_key

# n = int(input())


# def compare(s1, s2):
#     x1, y1 = s1
#     x2, y2 = s2

#     if x1 * y2 > x2 * y1:
#         return -1
#     if x1 * y2 == x2 * y1:
#         return 0

#     return 1

# ans = 0
# arr = []
# for i in range(n):
#     s = input()
#     opens, close = 0, 0
#     for c in s:
#         if s == '(':
#             opens += 1
#         else:
#             close += 1
#             ans += opens
    
#     arr.append((opens, close))

# arr.sort(key=cmp_to_key(compare))
# open_num = 0
# for opens, close in arr:
#     ans += opens * close
#     open_num += opens

# print(ans)

from functools import cmp_to_key

n = int(input())
brackets = []

ans = 0

def compare(b1, b2):
    open1, closed1 = b1
    open2, closed2 = b2

    if open1 * closed2 > open2 * closed1:
        return -1
    if open1 * closed2 < open2 * closed1:
        return 1
    return 0


for _ in range(n):
    s = input()
    open_num, closed_num = 0, 0 
    for char in s:
        if char == '(':
            open_num += 1
        else:
            closed_num += 1

            ans += open_num

    brackets.append((open_num, closed_num))

brackets.sort(key=cmp_to_key(compare))


open_sum = 0
for open_num, closed_num in brackets:
    ans += open_sum * closed_num

    open_sum += open_num

print(ans)