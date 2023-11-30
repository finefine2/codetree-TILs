# my solution 
# N,k,T = input().split()
# N = int(N) 
# words = [] 

# for _ in range(N): 
#     words.append(input()) 

# def in_T(): 
#     ans = []
#     for w in words: 
#         if w[:len(T)] == T: 
#             ans.append(w) 

#     return ans 
# t_word = in_T() 
# t_word.sort() 
# print(t_word[int(k)-1])

# given soluton 
N,k,T = input().split() 
N,k = int(N), int(k) 

# a가 b로 시작하는지 확인 
def starts_with(a,b): 
    # a가 b보다 길어야 함 
    if len(a) < len(b): 
        return False 
    # b 길이만큼 보고 같은 문자열을 포함하나 확인 
    return a[:len(b)] == b 
words = [] 
for _ in range(N): 
    w = input() 
    if starts_with(w,T): 
        words.append(w) 
words.sort() 
print(words[k-1])