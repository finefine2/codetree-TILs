N,k,T = input().split()
N = int(N) 
words = [] 

for _ in range(N): 
    words.append(input()) 

def in_T(): 
    ans = []
    for w in words: 
        if w[:len(T)] == T: 
            ans.append(w) 

    return ans 
t_word = in_T() 
t_word.sort() 
print(t_word[int(k)-1])